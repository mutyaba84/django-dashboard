# recipients/models.py

from django.db import models

class Recipient(models.Model):
    # Define choices for the network field
    NETWORK_CHOICES = [
        ('MTN', 'MTN'),
        ('Airtel', 'Airtel'),
      
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=15, unique=True)
    mobile_money_account = models.CharField(max_length=20)
    city = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=100, default='')
    verified = models.BooleanField(default=False)
    blocked = models.BooleanField(default=False)
    network = models.CharField(max_length=50, choices=NETWORK_CHOICES)  # Use choices parameter

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # Remaining methods...


    def verify_with_mtn(self):
        # Method to verify recipient details with MTN Mobile Money API
        # Implement API call to MTN for verification
        # Process response and return True if verified, False otherwise
        # Example:
        # api_response = mtn_api.verify_recipient(self.mobile_number, self.mobile_money_account)
        # return api_response['success']
        pass
    
    def verify_with_airtel(self):
        # Method to verify recipient details with Airtel Money API
        # Implement API call to Airtel for verification
        # Process response and return True if verified, False otherwise
        # Example:
        # api_response = airtel_api.verify_recipient(self.mobile_number, self.mobile_money_account)
        # return api_response['success']
        pass
    
    def verify_recipient(self):
        # Method to perform verification checks
        if self.blocked:
            return False  # Recipient is blocked, return False
        if self.network == 'MTN':
            # Check if recipient details match and verify with MTN
            if self.verify_with_mtn() and self.first_name.lower() in self.mobile_money_account.lower():
                self.verified = True
                self.save()
                return True
            else:
                return False
        elif self.network == 'Airtel':
            # Check if recipient details match and verify with Airtel
            if self.verify_with_airtel() and self.first_name.lower() in self.mobile_money_account.lower():
                self.verified = True
                self.save()
                return True
            else:
                return False
        else:
            return False  # Unknown network, cannot verify
    
    def can_receive_money(self):
        # Method to check if recipient is allowed to receive money
        return self.verified and not self.blocked
