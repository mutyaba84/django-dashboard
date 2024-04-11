# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Recipient
from .forms import RecipientForm

def add_recipient(request):
    if request.method == 'POST':
        form = RecipientForm(request.POST)
        if form.is_valid():
            recipient = form.save(commit=False)
            recipient.save()  # Save recipient even if not verified
            if recipient.verify_recipient():
                recipient.save()  # Save recipient again after verification
                return redirect('recipient_detail', pk=recipient.pk)  # Redirect to recipient detail view
            else:
                # Handle verification failure
                # Render form with error message
                return render(request, 'recipients/add_recipient.html', {'form': form, 'error': 'Recipient details could not be verified'})
    else:
        form = RecipientForm()
    return render(request, 'recipients/recipient_list.html', {'form': form})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipient
from .forms import RecipientForm

def edit_recipient(request, pk):
    recipient = get_object_or_404(Recipient, pk=pk)
    if request.method == 'POST':
        form = RecipientForm(request.POST, instance=recipient)
        if form.is_valid():
            recipient = form.save(commit=False)
            recipient.save()  # Save recipient even if not verified
            if recipient.verify_recipient():
                recipient.save()  # Save recipient again after verification
                return redirect('recipient_detail', pk=recipient.pk)  # Redirect to recipient detail view
            else:
                # Handle verification failure
                # Render form with error message
                return render(request, 'recipients/edit_recipient.html', {'form': form, 'error': 'Recipient details could not be verified'})
    else:
        form = RecipientForm(instance=recipient)
    return render(request, 'recipients/edit_recipient.html', {'form': form})


def delete_recipient(request, pk):
    recipient = get_object_or_404(Recipient, pk=pk)
    recipient.delete()
    return redirect('recipient_list')

def transfer_money(request, recipient_id):
    recipient = get_object_or_404(Recipient, pk=recipient_id)
    if recipient.can_receive_money():
        # Proceed with money transfer
        # Implement transfer logic here
        return JsonResponse({'message': 'Money transferred successfully'})
    else:
        # Recipient is not verified or blocked, handle accordingly
        return JsonResponse({'error': 'Transfer not allowed for this recipient'})

def recipient_list(request):
    recipients = Recipient.objects.all()
    return render(request, 'recipients/recipient_list.html', {'recipients': recipients})

def recipient_detail(request, pk):
    recipient = get_object_or_404(Recipient, pk=pk)
    return render(request, 'recipients/recipient_detail.html', {'recipient': recipient})

def save_exchange_rate(request):
    if request.method == 'POST':
        # Assuming you're receiving exchange rate data via POST request
        exchange_rate = request.POST.get('exchange_rate')

        # Example logic to save exchange rate to the database
        # This may involve creating a model to store exchange rates
        # For demonstration purposes, let's assume you have a model called ExchangeRate
        from .models import ExchangeRate
        exchange_rate_object, created = ExchangeRate.objects.get_or_create(rate=exchange_rate)

        if created:
            return JsonResponse({'message': 'Exchange rate saved successfully'})
        else:
            return JsonResponse({'message': 'Exchange rate already exists'})
    else:
        # Handle if request method is not POST
        return JsonResponse({'error': 'Invalid request method'})
