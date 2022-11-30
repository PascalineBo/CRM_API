import logging

from django.shortcuts import render
from rest_framework import status, exceptions
from rest_framework.permissions import IsAuthenticated
from authentication.permissions import \
    IsContractSalesContactOrDetailsOrReadOnly, IsControlling,\
    IsSales, IsControllingUsers
from .models import Contract
from .serializers import ContractSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from core.views import DestroyMixin


logging.basicConfig(filename='epic_logging.log', encoding='utf-8',
                    level=logging.INFO)


class ContractViewset(DestroyMixin, ModelViewSet):
    serializer_class = ContractSerializer

    permission_classes = [IsAuthenticated,
                          IsSales | IsControllingUsers,
                          IsContractSalesContactOrDetailsOrReadOnly |
                          IsControlling, ]

    def get_queryset(self, *args, **kwargs):
        return Contract.objects.all()

    def destroy(self, request, model_name="customer", *args, **kwargs):
        customer = self.get_object()
        return super().destroy(request, model_name, *args, **kwargs)
