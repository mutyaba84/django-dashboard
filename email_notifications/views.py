from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
#from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .models import CustomUser, PasswordReset

User = get_user_model()

EMAIL_TEMPLATE_DIR = 'emails/'

def send_email(subject, recipient_email, template_name, context):
    message = render_to_string(f'{EMAIL_TEMPLATE_DIR}{template_name}.html', context)
    email = EmailMessage(subject, message, to=[recipient_email])
    email.send()

def generate_activation_link(user):
    uid = urlsafe_base64_encode(force_bytes(user.pk)).decode()
    token = default_token_generator.make_token(user)
    return reverse('activate_account', kwargs={'uidb64': uid, 'token': token})

def send_activation_email(user):
    activation_link = generate_activation_link(user)
    subject = 'Account Activation'
    send_email(subject, user.email, 'activation', {'activation_link': activation_link})

def send_password_reset_email(user):
    reset_link = reverse('password_reset_confirm', kwargs={'uidb64': user.uidb64, 'token': user.token})
    subject = 'Password Reset'
    send_email(subject, user.email, 'password_reset', {'reset_link': reset_link})

def send_password_reset_success_email(user):
    subject = 'Password Reset Successful'
    send_email(subject, user.email, 'password_reset_success', {})

def activate_account(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your account has been activated successfully!')
    else:
        messages.error(request, 'Invalid activation link.')
    return redirect('login')

def password_reset_request(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            user = CustomUser.objects.get(email=email)
            password_reset = PasswordReset.objects.create(user=user, uidb64='', token='')  # Create a password reset instance
            send_password_reset_email(password_reset)
            messages.success(request, 'Password reset email has been sent.')
        except CustomUser.DoesNotExist:
            messages.error(request, 'This email address is not associated with any account.')
        return redirect('login')
    return render(request, "password_reset.html")

# Define the password reset confirm view
def password_reset_confirm(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        password_reset = PasswordReset.objects.get(uidb64=uid, token=token)
    except (TypeError, ValueError, OverflowError, PasswordReset.DoesNotExist):
        password_reset = None

    if password_reset is not None:
        # Implement your password reset confirmation logic here
        # For example, render a password reset form
        return render(request, 'password_reset_confirm.html', {'password_reset': password_reset})
    else:
        messages.error(request, 'Invalid password reset link.')
        return redirect('login')

# Define the password reset confirm submission view
def password_reset_confirm_submit(request, uidb64, token):
    if request.method == "POST":
        # Retrieve the password reset instance based on uidb64 and token
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            password_reset = PasswordReset.objects.get(uidb64=uid, token=token)
        except (TypeError, ValueError, OverflowError, PasswordReset.DoesNotExist):
            password_reset = None

        if password_reset is not None:
            # Implement your password reset confirmation submission logic here
            # For example, update the user's password
            new_password = request.POST.get('new_password')
            password_reset.user.set_password(new_password)
            password_reset.user.save()
            # Delete the password reset instance after successful password reset
            password_reset.delete()
            messages.success(request, 'Your password has been reset successfully.')
            return redirect('login')
        else:
            messages.error(request, 'Invalid password reset link.')
    return redirect('login')
