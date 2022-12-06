from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Contract

User = get_user_model()


class ContractSerializer(serializers.ModelSerializer):
    contract_company = serializers.CharField(
        source='contract_customer.company_name',
        required=False)

    class Meta:
        model = Contract
        fields = ['id', 'contract_company',
                  'contract_customer', 'price',
                  'signed', 'payment_due', 'created_time']
