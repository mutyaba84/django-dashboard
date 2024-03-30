from django.contrib import admin
from .models import ExchangeRate, ConversionHistory

@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ['from_currency', 'to_currency', 'rate']
    search_fields = ['from_currency', 'to_currency']
    list_filter = ['from_currency', 'to_currency']

@admin.register(ConversionHistory)
class ConversionHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'timestamp', 'amount', 'from_currency', 'to_currency', 'converted_amount']
    search_fields = ['user__username', 'from_currency', 'to_currency']
    list_filter = ['user', 'from_currency', 'to_currency', 'timestamp']
