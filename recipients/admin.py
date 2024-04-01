
from django.contrib import admin
from .models import Recipient

@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'mobile_number', 'mobile_account_number', 'city', 'country']
    search_fields = ['first_name', 'last_name', 'mobile_number', 'mobile_account_number', 'city', 'country']
