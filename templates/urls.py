# transfers/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('initiate/', views.initiate_transfer, name='initiate_transfer'),
    # Add more URL patterns as needed
]
