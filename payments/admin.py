from django.contrib import admin
from .models import PaymentMethod, Transaction, SavedCard

admin.site.register(PaymentMethod)
admin.site.register(Transaction)
admin.site.register(SavedCard)
