## urls.py

from django.urls import path
from . import views

urlpatterns = [
   
    
    path('', views.recipient_list, name='recipient_list'),
    path('add/', views.add_recipient, name='add_recipient'),
    path('<int:pk>/', views.recipient_detail, name='recipient_detail'),
    path('<int:pk>/edit/', views.edit_recipient, name='edit_recipient'),
    path('<int:pk>/delete/', views.delete_recipient, name='delete_recipient'),
    path('<int:recipient_id>/transfer/', views.transfer_money, name='transfer_money'),
]
