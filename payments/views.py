#payments views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PaymentMethod, Transaction, SavedCard
from .forms import PaymentMethodForm, TransactionForm, SavedCardForm



@login_required
def add_payment_method(request):
    if request.method == 'POST':
        form = PaymentMethodForm(request.POST)
        if form.is_valid():
            payment_method = form.save(commit=False)
            payment_method.user = request.user
            payment_method.save()
            return redirect('payment_methods')  # Assuming you have a URL named 'payment_methods' to redirect to
    else:
        form = PaymentMethodForm()
    return render(request, 'payments/add_payment_method.html', {'form': form})

@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('transactions')  # Assuming you have a URL named 'transactions' to redirect to
    else:
        form = TransactionForm()
    return render(request, 'payments/add_transaction.html', {'form': form})

@login_required
def add_saved_card(request):
    if request.method == 'POST':
        form = SavedCardForm(request.POST)
        if form.is_valid():
            saved_card = form.save(commit=False)
            saved_card.user = request.user
            saved_card.save()
            return redirect('payments/saved_cards')  # Assuming you have a URL named 'saved_cards' to redirect to
    else:
        form = SavedCardForm()
    return render(request, 'payments/add_saved_card.html', {'form': form})


@login_required
def edit_saved_card(request, card_id):
    saved_card = SavedCard.objects.get(id=card_id)
    if request.method == 'POST':
        form = SavedCardForm(request.POST, instance=saved_card)
        if form.is_valid():
            form.save()
            return redirect('payments/saved_cards')
    else:
        form = SavedCardForm(instance=saved_card)
    return render(request, 'payments/edit_saved_card.html', {'form': form})

def saved_cards(request):
    saved_cards = SavedCard.objects.all()  # Retrieve all saved cards from the database
    return render(request, 'payments/saved_cards.html', {'saved_cards': saved_cards})
