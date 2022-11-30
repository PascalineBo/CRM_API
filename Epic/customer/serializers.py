from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework import exceptions
from .models import Customer

User = get_user_model()

class CustomerSerializer(serializers.ModelSerializer):

    sales_contact_name = serializers.CharField(source='sales_contact.username',
                                                required=False)

    class Meta:
        model = Customer
        fields = ['sales_contact_name','active_customer',
                  'customer_first_name','customer_last_name',
                  'customer_email','customer_phone',
                  'customer_adress','company_name',
                  'sales_contact','id']
