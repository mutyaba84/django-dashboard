from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, smart_text  # Updated import statement
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import redirect

User = get_user_model()

def generate_token(user):
    """
    Generate a token for the given user.
    """
    uid = urlsafe_base64_encode(force_bytes(user.pk)).decode()
    token = default_token_generator.make_token(user)
    return uid, token

def send_activation_email(user):
    """
    Send an account activation email to the user.
    """
    uid, token = generate_token(user)
    activation_link = reverse('activate_account', kwargs={'uidb64': uid, 'token': token})
    subject = 'Account Activation'
    message = render_to_string('activation_email.html', {'activation_link': activation_link})
    send_mail(subject, '', None, [user.email], html_message=message)

def send_password_reset_email(user):
    """
    Send a password reset email to the user.
    """
    uid, token = generate_token(user)
    reset_link = reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
    subject = 'Password Reset'
    message = render_to_string('password_reset_email.html', {'reset_link': reset_link})
    send_mail(subject, '', None, [user.email], html_message=message)

def activate_account(request, uidb64, token):
    """
    Activate the user account based on the activation link.
    """
    try:
        uid = smart_text(urlsafe_base64_decode(uidb64))  # Updated force_text to smart_text
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your account has been activated successfully!')
    else:
        messages.error(request, 'Invalid activation link.')
    return redirect('login')

