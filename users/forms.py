# forms.py
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'middle_name', 'current_address', 'previous_address', 'is_disabled', 'disablement_timestamp']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['is_disabled'].widget.attrs['disabled'] = True  # Disable the is_disabled field to prevent modification in the form
        self.fields['disablement_timestamp'].widget.attrs['readonly'] = True  # Make the disablement_timestamp field read-only
