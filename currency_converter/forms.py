# forms.py

from django import forms
from .models import ExchangeRate


class ExchangeRateForm(forms.Form):
    currency_from = forms.CharField(max_length=3)
    currency_to = forms.CharField(max_length=3)
    rate = forms.DecimalField(max_digits=10, decimal_places=2)
