# models.py in payments app
from django.db import models
from django.contrib.auth import get_user_model

class PaymentMethod(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    expiration_date = models.DateField()
    cvc = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.user.username} - {self.card_number}'

class Transaction(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.amount}'
