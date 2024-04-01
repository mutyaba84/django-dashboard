# forms.py in recipients app
from django import forms
from .models import Recipient

class RecipientForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = ['first_name', 'last_name', 'mobile_number', 'mobile_account_number', 'city', 'country']
