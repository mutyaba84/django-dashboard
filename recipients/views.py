# views.py in recipients app
from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipient
from .forms import RecipientForm
from .services import MobileServiceProvider  # Import mobile service provider integration

def update_recipient(request, recipient_id):
    recipient = get_object_or_404(Recipient, pk=recipient_id)
    if request.method == 'POST':
        form = RecipientForm(request.POST, instance=recipient)
        if form.is_valid():
            # Get form data
            phone_number = form.cleaned_data['phone_number']
            mobile_account_number = form.cleaned_data['mobile_account_number']
            mobile_network = form.cleaned_data['mobile_network']
            
            # Perform phone number verification
            if MobileServiceProvider.verify_phone_number(phone_number, mobile_account_number, mobile_network):
                form.save()
                return redirect('recipient_list')
            else:
                form.add_error(None, 'Phone number verification failed.')
    else:
        form = RecipientForm(instance=recipient)
    return render(request, 'recipients/update_recipient.html', {'form': form})
