# views.py

from django.shortcuts import render, get_object_or_404
from .forms import ExchangeRateForm
from .models import ExchangeRate

def exchange_rate_form(request):
    converted_amount = None
    
    if request.method == 'POST':
        form = ExchangeRateForm(request.POST)
        if form.is_valid():
            exchange_rate_data = form.cleaned_data
            currency_from = exchange_rate_data['currency_from']
            currency_to = exchange_rate_data['currency_to']
            rate = get_exchange_rate(currency_from, currency_to)
            if rate is not None:
                amount = exchange_rate_data['rate']  # Amount to convert
                converted_amount = amount * rate
    else:
        form = ExchangeRateForm()
    
    return render(request, 'exchange_rate_form.html', {'form': form, 'converted_amount': converted_amount})

def get_exchange_rate(currency_from, currency_to):
    exchange_rate = get_object_or_404(ExchangeRate, currency_from=currency_from, currency_to=currency_to)
    return exchange_rate.rate if exchange_rate else None
