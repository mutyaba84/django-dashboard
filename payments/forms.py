from django import forms
from .models import PaymentMethod, Transaction, SavedCard

class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = ['card_number', 'expiration_date', 'cvc']
        labels = {
            'card_number': 'Card Number:',
            'expiration_date': 'Expiration Date:',
            'cvc': 'CVC:'
        }
        help_texts = {
            'card_number': 'Enter your card number',
            'expiration_date': 'Enter the expiration date of your card',
            'cvc': 'Enter the CVC code on the back of your card'
        }
        widgets = {
            'card_number': forms.TextInput(attrs={'placeholder': 'Enter card number'}),
            'expiration_date': forms.DateInput(attrs={'placeholder': 'MM/YYYY'}),
            'cvc': forms.TextInput(attrs={'placeholder': 'Enter CVC'})
        }

    def clean_card_number(self):
        card_number = self.cleaned_data['card_number']
        # Implement additional validation if needed
        return card_number

    def clean_cvc(self):
        cvc = self.cleaned_data['cvc']
        # Implement additional validation if needed
        return cvc

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'description']
        labels = {
            'amount': 'Amount:',
            'description': 'Description:'
        }
        help_texts = {
            'amount': 'Enter the transaction amount',
            'description': 'Enter a description for the transaction'
        }
        widgets = {
            'amount': forms.NumberInput(attrs={'placeholder': 'Enter amount'}),
            'description': forms.Textarea(attrs={'rows': 3, 'cols': 40, 'placeholder': 'Enter description'})
        }

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        # Implement additional validation if needed
        return amount

    def clean_description(self):
        description = self.cleaned_data['description']
        # Implement additional validation if needed
        return description

class SavedCardForm(forms.ModelForm):
    class Meta:
        model = SavedCard
        fields = ['card_number', 'expiration_date', 'cvc']
        labels = {
            'card_number': 'Card Number:',
            'expiration_date': 'Expiration Date:',
            'cvc': 'CVC:'
        }
        help_texts = {
            'card_number': 'Enter your card number',
            'expiration_date': 'Enter the expiration date of your card',
            'cvc': 'Enter the CVC code on the back of your card'
        }
        widgets = {
            'card_number': forms.TextInput(attrs={'placeholder': 'Enter card number'}),
            'expiration_date': forms.DateInput(attrs={'placeholder': 'MM/YYYY'}),
            'cvc': forms.TextInput(attrs={'placeholder': 'Enter CVC'})
        }

    def clean_card_number(self):
        card_number = self.cleaned_data['card_number']
        # Implement additional validation if needed
        return card_number

    def clean_cvc(self):
        cvc = self.cleaned_data['cvc']
        # Implement additional validation if needed
        return cvc
