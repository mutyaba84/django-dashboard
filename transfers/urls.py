from django.urls import path
from . import views

app_name = 'transfers'

urlpatterns = [
     path('transfers/', views.initiate_transfer, name='transfer'),
    # Add more URL patterns as needed
]
