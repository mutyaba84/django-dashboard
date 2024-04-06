# urls.py
from django.urls import path
from .views import (
    update_user_profile, 
    delete_user_profile, 
    disable_user_profile, 
    reactivate_user_profile,
)

urlpatterns = [
    path('profile/<int:user_id>/update/', update_user_profile, name='update_user_profile'),
    path('profile/<int:user_id>/delete/', delete_user_profile, name='delete_user_profile'),
    path('profile/<int:user_id>/disable/', disable_user_profile, name='disable_user_profile'),
    path('profile/<int:user_id>/reactivate/', reactivate_user_profile, name='reactivate_user_profile'),
]
