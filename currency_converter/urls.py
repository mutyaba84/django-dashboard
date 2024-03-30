from django.urls import path
from . import views

urlpatterns = [
    path('', views.convert_currency, name='convert_currency'),
    path('history/', views.conversion_history, name='convert_history'),
]
