# admin.py

from django.contrib import admin
from .models import ExchangeRate

class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('currency_from', 'currency_to', 'rate')
    search_fields = ('currency_from', 'currency_to')

admin.site.register(ExchangeRate, ExchangeRateAdmin)
