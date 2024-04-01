from django import forms
from .models import PaymentMethod, Transaction, SavedCard  # Import SavedCard model along with others

class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = ['card_number', 'expiration_date', 'cvc']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction  # Reference the Transaction model
        fields = ['amount', 'description']


class SavedCardForm(forms.ModelForm):
    class Meta:
        model = SavedCard
        fields = ['card_number', 'expiration_date', 'cvc']