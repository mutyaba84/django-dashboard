from django.db import models
from django.contrib.auth import get_user_model

class MobileTransaction(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    recipient = models.CharField(max_length=100)
    provider = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.amount} to {self.recipient}'
