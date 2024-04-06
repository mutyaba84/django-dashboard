# models.py
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    current_address = models.CharField(max_length=255)
    previous_address = models.CharField(max_length=255, blank=True, null=True)
    is_disabled = models.BooleanField(default=False)
    disablement_timestamp = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    def delete_user(self):
        self.user.delete()

    def disable_user(self):
        self.is_disabled = True
        self.disablement_timestamp = timezone.now()
        self.save()

    def reactivate_user(self):
        self.is_disabled = False
        self.disablement_timestamp = None
        self.save()
