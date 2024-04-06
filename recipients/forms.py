# forms.py

from django import forms
from .models import Recipient
import requests

class RecipientForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = ['first_name', 'last_name', 'mobile_number', 'mobile_money_account', 'city', 'country', 'network']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'mobile_number': 'Mobile Number',
            'mobile_money_account': 'Mobile Account Number',
            'city': 'City',
            'country': 'Country',
            'network': 'Network'
        }
       
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name'}),
            'mobile_number': forms.TextInput(attrs={'placeholder': 'Enter your mobile number'}),
            'mobile_money_account': forms.TextInput(attrs={'placeholder': 'Enter your mobile account number'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter your city'}),
            'country': forms.TextInput(attrs={'placeholder': 'Enter your country'}),
        }

    def is_verified_with_mtn(self, mobile_number):
        # Implement verification with MTN API
        try:
            response = requests.get('https://mtn-api.com/verify', params={'mobile_number': mobile_number})
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'verified':
                    return True
        except Exception as e:
            print(f"Error verifying with MTN: {e}")
        return False

    def is_verified_with_airtel(self, mobile_number):
        # Implement verification with Airtel API
        try:
            response = requests.get('https://airtel-api.com/verify', params={'mobile_number': mobile_number})
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'verified':
                    return True
        except Exception as e:
            print(f"Error verifying with Airtel: {e}")
        return False

    def clean(self):
        cleaned_data = super().clean()
        mobile_number = cleaned_data.get('mobile_number')
        network = cleaned_data.get('network')

        # Perform custom validation to set the network automatically based on verification
        if mobile_number:
            if self.is_verified_with_mtn(mobile_number):
                cleaned_data['network'] = 'MTN'
            elif self.is_verified_with_airtel(mobile_number):
                cleaned_data['network'] = 'Airtel'
            else:
                self.add_error('network', 'The network for this mobile number could not be determined.')

        return cleaned_data
