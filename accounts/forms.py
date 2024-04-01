# forms.py

from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']  # Adjust fields as needed

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize form fields if necessary
