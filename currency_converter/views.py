from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ConversionHistory
from django.contrib.auth.decorators import login_required
import os
import requests

@login_required
def convert_currency(request):
    if request.method == 'POST':
        amount = float(request.POST.get('amount', 0))
        from_currency = request.POST.get('from_currency', '')
        to_currency = request.POST.get('to_currency', '')

        # Fetch currency data and perform conversion
        from_currency_data = get_currency_data(from_currency)
        to_currency_data = get_currency_data(to_currency)

        if from_currency_data and to_currency_data:
            conversion_result = perform_currency_conversion(amount, from_currency, to_currency)

            if 'error' in conversion_result:
                # Handle conversion error
                messages.error(request, conversion_result['error'])
            else:
                # Save conversion history
                try:
                    ConversionHistory.objects.create(
                        user=request.user,
                        amount=amount,
                        from_currency=from_currency,
                        to_currency=to_currency,
                        converted_amount=conversion_result['converted_amount']
                    )
                    messages.success(request, 'Conversion successful.')
                    # Add conversion result to the context
                    context = {'conversion_result': conversion_result['converted_amount']}
                    return render(request, 'currency_converter/convert_currency.html', context)
                except Exception as e:
                    # Log the exception for debugging
                    print("Error saving conversion history:", e)
                    messages.error(request, 'Failed to save conversion history.')

            # Redirect to the same page or render a response
            return redirect('convert_currency')
        else:
            messages.error(request, 'Failed to fetch currency information.')

    return render(request, 'currency_converter/convert_currency.html')

def get_currency_data(currency_code):
    try:
        response = requests.get(f'https://restcountries.com/v3/alpha/{currency_code}')
        data = response.json()
        if response.status_code == 200:
            currency_data = {
                'symbol': data[0]['currencies'][0]['symbol'],
                'flag': data[0]['flags'][0]
            }
            return currency_data
    except Exception as e:
        print(e)
    return None

def perform_currency_conversion(amount, from_currency, to_currency):
    # Replace with your API key
    api_key = os.getenv('EXCHANGE_RATE_API_KEY')

    # Example using exchange rate API
    url = f'https://api.exchangeratesapi.io/latest?base={from_currency}&symbols={to_currency}&access_key={api_key}'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        try:
            conversion_rate = data['rates'][to_currency]
            converted_amount = amount * conversion_rate
            return {'converted_amount': converted_amount}
        except KeyError:
            return {'error': 'Invalid currency code or conversion rate not available.'}
    else:
        return {'error': 'Failed to fetch exchange rates. Please try again later.'}

@login_required
def conversion_history(request):
    history = ConversionHistory.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'currency_converter/conversion_history.html', {'history': history})
