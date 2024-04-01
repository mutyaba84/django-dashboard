# models.py in the payments app
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator

class PaymentMethod(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16, validators=[MinLengthValidator(16)])
    expiration_date = models.DateField()
    cvc = models.CharField(max_length=3, validators=[MinLengthValidator(3)])
    # Add other fields as needed, like cardholder name, etc.

    def __str__(self):
        return f'{self.user.username} - {self.masked_card_number()}'

    def masked_card_number(self):
        return f'**** **** **** {self.card_number[-4:]}'

class Transaction(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.amount}'

class SavedCard(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16, validators=[MinLengthValidator(16)])
    expiration_date = models.DateField()
    cvc = models.CharField(max_length=3, validators=[MinLengthValidator(3)])
    # Add other fields as needed
    
    def __str__(self):
        return f'{self.user.username} - {self.masked_card_number()}'

    def masked_card_number(self):
        return f'**** **** **** {self.card_number[-4:]}'


