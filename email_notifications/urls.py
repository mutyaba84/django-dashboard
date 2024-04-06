from django.urls import path
from . import views

urlpatterns = [
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('activate/<uidb64>/<token>/', views.activate_account, name='activate_account'),
    # Add other URLs as needed
]
