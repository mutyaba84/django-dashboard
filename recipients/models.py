from django.db import models
from django.contrib.auth import get_user_model



class Recipient(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=15)
    mobile_account_number = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    
  

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
