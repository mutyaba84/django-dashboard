from django.urls import path
from . import views

urlpatterns = [
    path('add-payment-method/', views.add_payment_method, name='add_payment_method'),
    path('add-transaction/', views.add_transaction, name='add_transaction'),
    path('add-saved-card/', views.add_saved_card, name='add_saved_card'),
    path('edit-saved-card/<int:card_id>/', views.edit_saved_card, name='edit_saved_card'),
    path('saved-cards/', views.saved_cards, name='saved_cards'),
]
