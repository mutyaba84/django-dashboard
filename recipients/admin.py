# admin.py

from django.contrib import admin
from .models import Recipient

@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = [ 'mobile_number', 'mobile_money_account', 'verified', 'blocked', 'network']
    search_fields = [ 'mobile_number', 'mobile_money_account']
    list_filter = ['verified', 'blocked', 'network']
    actions = ['verify_recipients']

    def verify_recipients(self, request, queryset):
        for recipient in queryset:
            recipient.verify_recipient()
        self.message_user(request, "Selected recipients verified successfully.")

    verify_recipients.short_description = "Verify selected recipients"
