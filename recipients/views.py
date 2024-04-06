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
                return redirect('recipient_detail', pk=recipient.pk)
            else:
                # Handle verification failure
                # Render form with error message
                return render(request, 'recipients/recipient_detail.html', {'form': form, 'error': 'Recipient details could not be verified'})
    else:
        form = RecipientForm()
    return render(request, 'recipients/recipient_detail.html', {'form': form})

def edit_recipient(request, pk):
    recipient = get_object_or_404(Recipient, pk=pk)
    if request.method == 'POST':
        form = RecipientForm(request.POST, instance=recipient)
        if form.is_valid():
            recipient = form.save(commit=False)
            recipient.save()  # Save recipient even if not verified
            if recipient.verify_recipient():
                recipient.save()  # Save recipient again after verification
                return redirect('recipient_detail', pk=recipient.pk)
            else:
                # Handle verification failure
                # Render form with error message
                return render(request, 'recipients/recipient_detail.html', {'form': form, 'error': 'Recipient details could not be verified'})
    else:
        form = RecipientForm(instance=recipient)
    return render(request, 'recipients/recipient_detail.html', {'form': form})

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
    return render(request, 'recipients/recipient_detail.html', {'recipients': recipients})

def recipient_detail(request, pk):
    recipient = get_object_or_404(Recipient, pk=pk)
    return render(request, 'recipients/recipient_detail.html', {'recipient': recipient})
