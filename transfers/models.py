# transfers/models.py
from django.db import models
from django.contrib.auth.models import User

class Transfer(models.Model):
    sender = models.ForeignKey(User, related_name='transfers_sent', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='transfers_received', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, default='pending')  # pending, completed, failed, etc.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return f"Transfer from {self.sender} to {self.recipient} - {self.amount}"
