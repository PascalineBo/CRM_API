import logging

from django.shortcuts import render
from django.db.models import Q
from rest_framework import status, exceptions
from rest_framework.permissions import IsAuthenticated
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from authentication.models import User
from rest_framework.permissions import IsAuthenticated
from authentication.permissions import IsSales,IsSupport,\
    IsCustomerSalesContactOrDetailsOrReadOnly,IsControlling
from core.views import DestroyMixin


logging.basicConfig(filename='epic_logging.log', encoding='utf-8',
                    level=logging.INFO)


class CustomerViewset(DestroyMixin, ModelViewSet):
    serializer_class = CustomerSerializer

    permission_classes = [IsAuthenticated,
                          IsSales|IsControlling,
                          IsCustomerSalesContactOrDetailsOrReadOnly]


    def get_queryset(self, *args, **kwargs):
        # user = self.request.user
        # controllers = User.objects.filter(position='CONTROLLING').all()
        # sales = User.objects.filter(position='SALES').all()
        # if user in controllers:
            # return Customer.objects.all()
        # return Customer.objects.filter(sales_contact_id=user.id)
        queryset = Customer.objects.all()
        company_name = self.request.GET.get('name')
        if company_name is not None:
            queryset = queryset.filter(company_name=company_name)
        customer_email = self.request.GET.get('e-mail')
        if customer_email is not None:
            queryset = queryset.filter(customer_email=customer_email)
        return queryset


    def destroy(self, request, model_name="customer", *args, **kwargs):
        customer = self.get_object()
        return super().destroy(request, model_name, *args, **kwargs)



