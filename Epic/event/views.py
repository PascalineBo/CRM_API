import logging

from django.shortcuts import render
from rest_framework import status, exceptions
from rest_framework.permissions import IsAuthenticated
from .models import Event
from customer.models import Customer
from .serializers import EventSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from authentication.permissions import \
    IsControlling,IsSales, IsSupport, IsEventSalesOrControllerOrEventSupport
from core.views import DestroyMixin
from rest_framework import filters


logging.basicConfig(filename='epic_logging.log', encoding='utf-8',
                    level=logging.INFO)


class EventViewset(DestroyMixin, ModelViewSet):
    serializer_class = EventSerializer

    permission_classes = [ IsAuthenticated ,
                          IsEventSalesOrControllerOrEventSupport]

    # 'event date' filter
    filter_backends = [filters.SearchFilter]
    search_fields = ['event_date']

    def get_queryset(self, *args, **kwargs):
        queryset = Event.objects.all()

        customer_queryset = Customer.objects.all()

        # company name filter
        company_name = self.request.GET.get('name')
        if company_name is not None:
            company_queryset = customer_queryset.filter(
                company_name=company_name)
            if len(company_queryset) > 0:
                event_customer = company_queryset[0]
                queryset = queryset.filter(event_customer=event_customer)

        # customer email filter
        customer_email =  self.request.GET.get('e-mail')
        if customer_email is not None:
            customer_queryset = customer_queryset.filter(
                customer_email=customer_email)
            if len(customer_queryset) > 0:
                event_customer = customer_queryset[0]
                queryset = queryset.filter(event_customer=event_customer)

        return queryset

    def destroy(self, request, model_name="event", *args, **kwargs):
        event = self.get_object()
        return super().destroy(request, model_name, *args, **kwargs)

