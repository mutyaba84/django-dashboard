from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.mail import EmailMessage
from django.db import models
from django.contrib import messages
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
#from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email=email, username=username, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add any additional fields or methods as needed
    
    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'

# Specify unique related names for groups and user_permissions fields
CustomUser._meta.get_field('groups').remote_field.related_name = 'customuser_groups'
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'customuser_user_permissions'

class PasswordReset(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='password_resets')
    uidb64 = models.CharField(_('uidb64'), max_length=255)
    token = models.CharField(_('token'), max_length=255)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('password reset')
        verbose_name_plural = _('password resets')

    def __str__(self):
        return f'Password reset for {self.user.email}'

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
            send_password_reset_email(user)
            messages.success(request, 'Password reset email has been sent.')
        except CustomUser.DoesNotExist:
            messages.error(request, 'This email address is not associated with any account.')
        return redirect('login')
    return render(request, "password_reset.html")
