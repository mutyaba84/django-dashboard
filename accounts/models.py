from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class User(AbstractUser):
    # Define your custom fields and methods here

    class Meta:
        pass

    # Add custom related_name attributes to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_groups',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_permissions',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
    )



class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return self.user.username

    def update_profile_picture(self, profile_picture):
        self.profile_picture = profile_picture
        self.save()

    def get_current_information(self):
        return {
            'username': self.user.username,
            'email': self.user.email,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'address': self.user.address,
            'profile_picture': self.profile_picture.url if self.profile_picture else None
        }

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()
