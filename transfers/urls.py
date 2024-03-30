from django.urls import path
from . import views

app_name = 'transfers'

urlpatterns = [
    path('', views.initiate_transfer, name='initiate_transfer'),
    # Add more URL patterns as needed
]
