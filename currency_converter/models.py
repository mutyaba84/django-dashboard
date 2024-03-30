# Inside currency_converter/models.py
from django.db import models
from django.contrib.auth.models import User

class ExchangeRate(models.Model):
    from_currency = models.CharField(max_length=3)
    to_currency = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=10, decimal_places=6)

    def __str__(self):
        return f"{self.from_currency}/{self.to_currency}: {self.rate}"

class ConversionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=20, decimal_places=6)
    from_currency = models.CharField(max_length=3)
    to_currency = models.CharField(max_length=3)
    converted_amount = models.DecimalField(max_digits=20, decimal_places=6)

    def __str__(self):
        return f"Conversion by {self.user.username} at {self.timestamp}"
