# Inside currency_converter/serializers.py

from rest_framework import serializers
from .models import ExchangeRate

class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = ['from_currency', 'to_currency', 'rate']
