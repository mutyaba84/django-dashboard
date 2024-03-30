# transfers/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TransferForm

def initiate_transfer(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            transfer = form.save(commit=False)
            transfer.sender = request.user
            print("Transfer object before saving:", transfer)  # Debugging
            transfer.save()
            print("Transfer object after saving:", transfer)  # Debugging
            messages.success(request, 'Transfer initiated successfully.')
            return redirect('transfer_prompt')
        else:
            print("Form errors:", form.errors)  # Debugging
            messages.error(request, 'Invalid transfer details. Please try again.')
    else:
        form = TransferForm()
    return render(request, 'transfers/initiate_transfer.html', {'form': form})
