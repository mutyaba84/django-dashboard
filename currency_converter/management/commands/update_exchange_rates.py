
# your_app/management/commands/fetch_country_currency_exchange_rates.py

from django.core.management.base import BaseCommand
from currency_converter.models import CountryCurrencyCode, CurrencyExchangeRate
import requests

class Command(BaseCommand):
    help = 'Fetches country and currency codes along with exchange rates from an API and populates the database'

    def add_arguments(self, parser):
        parser.add_argument('--api-url', type=str, help='API URL for fetching country, currency codes, and exchange rates')

    def handle(self, *args, **kwargs):
        api_url = kwargs.get('https://api.exchangerate-api.com/v4/latest/USD') or 'https://example.com/country_currency_exchange_rates'  # Default API URL
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an exception for bad responses (e.g., 404)
            data = response.json()

            # Process the API response and populate the database
            for entry in data:
                country_name = entry.get('country')
                currency_code = entry.get('currency')
                exchange_rate = entry.get('exchange_rate')

                if country_name and currency_code and exchange_rate:
                    # Get or create CountryCurrencyCode object
                    country_currency, _ = CountryCurrencyCode.objects.get_or_create(
                        country_name=country_name, currency_code=currency_code
                    )

                    # Create CurrencyExchangeRate object
                    CurrencyExchangeRate.objects.create(
                        country_currency=country_currency, exchange_rate=exchange_rate
                    )

                    self.stdout.write(self.style.SUCCESS(f"Added exchange rate: {exchange_rate} for {country_currency}"))

            self.stdout.write(self.style.SUCCESS('Successfully fetched and populated country, currency codes, and exchange rates'))

        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f"Error fetching data from API: {e}"))
