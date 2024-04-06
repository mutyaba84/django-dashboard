
from django.contrib import admin
# admin.py
from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'current_address', 'is_disabled']
    list_filter = ['is_disabled']
    search_fields = ['user__username', 'first_name', 'last_name']

admin.site.register(UserProfile, UserProfileAdmin)
