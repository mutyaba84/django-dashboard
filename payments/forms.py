# forms.py in payments app
from django import forms
from .models import PaymentMethod

class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = ['card_number', 'expiration_date', 'cvc']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'description']
