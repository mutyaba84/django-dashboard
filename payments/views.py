# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile, SavedCard
from .forms import SavedCardForm

@login_required
def add_saved_card(request):
    if request.method == 'POST':
        form = SavedCardForm(request.POST)
        if form.is_valid():
            saved_card = form.save(commit=False)
            saved_card.user_profile = request.user.userprofile
            saved_card.save()
            return redirect('saved_cards')
    else:
        form = SavedCardForm()
    return render(request, 'add_saved_card.html', {'form': form})

@login_required
def edit_saved_card(request, card_id):
    saved_card = SavedCard.objects.get(id=card_id)
    if request.method == 'POST':
        form = SavedCardForm(request.POST, instance=saved_card)
        if form.is_valid():
            form.save()
            return redirect('saved_cards')
    else:
        form = SavedCardForm(instance=saved_card)
    return render(request, 'edit_saved_card.html', {'form': form})

@login_required
def saved_cards(request):
    saved_cards = SavedCard.objects.filter(user_profile=request.user.userprofile)
    return render(request, 'saved_cards.html', {'saved_cards': saved_cards})
