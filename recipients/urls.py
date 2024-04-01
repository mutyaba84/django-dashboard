# urls.py in recipients app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipient_list, name='recipient_list'),
    path('<int:recipient_id>/update/', views.update_recipient, name='update_recipient'),
    path('<int:recipient_id>/delete/', views.delete_recipient, name='delete_recipient'),
]
