from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Event

User = get_user_model()


class EventSerializer(serializers.ModelSerializer):
    event_customer_name = serializers.CharField(
        source='event_customer.company_name', required=False)
    support_contact_name = serializers.CharField(
        source='event_support_contact.username', required=False)
    sales_contact_name = serializers.CharField(
        source='event_sales_contact.username', required=False)

    class Meta:
        model = Event
        fields = ['event_customer_name', 'support_contact_name',
                  'sales_contact_name', 'event_name',
                  'event_date', 'event_place',
                  'event_status', 'notes',
                  'attendees', 'related_contract',
                  'event_customer', 'event_support_contact',
                  'event_sales_contact', 'id']
