# service_providers/views.py
from django.shortcuts import render
from django.http import JsonResponse
import requests

def transfer_to_mtn(request):
    # Logic to handle money transfer to MTN
    if request.method == 'POST':
        # Process form data
        amount = request.POST.get('amount')
        recipient = request.POST.get('recipient')

        # Make API request to MTN money transfer endpoint
        response = requests.post('https://api.mtn.com/v1/transfer', json={'amount': amount, 'recipient': recipient})

        # Check response status and return appropriate message
        if response.status_code == 200:
            return JsonResponse({'message': 'Money transferred to MTN successfully'})
        else:
            return JsonResponse({'error': 'Failed to transfer money to MTN'})

    return render(request, 'service_providers/transfer_to_mtn.html')

def transfer_to_airtel(request):
    # Logic to handle money transfer to Airtel
    if request.method == 'POST':
        # Process form data
        amount = request.POST.get('amount')
        recipient = request.POST.get('recipient')

        # Make API request to Airtel money transfer endpoint
        response = requests.post('https://api.airtel.com/v1/transfer', json={'amount': amount, 'recipient': recipient})

        # Check response status and return appropriate message
        if response.status_code == 200:
            return JsonResponse({'message': 'Money transferred to Airtel successfully'})
        else:
            return JsonResponse({'error': 'Failed to transfer money to Airtel'})

    return render(request, 'service_providers/transfer_to_airtel.html')
