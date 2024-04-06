from django.urls import path
from . import views

urlpatterns = [
    path('transfer-to-mtn/', views.transfer_to_mtn, name='transfer_to_mtn'),
    path('transfer-to-airtel/', views.transfer_to_airtel, name='transfer_to_airtel'),
]
