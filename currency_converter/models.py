# models.py

from django.db import models

class ExchangeRate(models.Model):
    currency_from = models.CharField(max_length=3)  # Assuming 3-character currency codes
    currency_to = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=10, decimal_places=2)  # Assuming rate with 2 decimal places



    class Meta:
        unique_together = ('currency_from', 'currency_to')

    def __str__(self):
        return f'{self.currency_from }/{self.currency_to}: {self.rate}'
