# tasks.py

from celery import shared_task
from currency_converter.models import ExchangeRate
import requests

@shared_task
def update_exchange_rates():
    try:
        # Make a request to the external API to fetch exchange rates
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        data = response.json()

        # Extract exchange rates from the response
        exchange_rates = data.get('rates')

        # Save exchange rates in the database
        for currency, rate in exchange_rates.items():
            ExchangeRate.objects.update_or_create(
                from_currency='EUR',
                to_currency=currency,
                defaults={'rate': rate}
            )

        print('Exchange rates updated successfully')

    except Exception as e:
        print(f'Failed to update exchange rates: {e}')
