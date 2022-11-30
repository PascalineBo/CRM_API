import logging

from django.shortcuts import render
from rest_framework import status, exceptions
from rest_framework.permissions import IsAuthenticated
from .models import Contract
from .serializers import ContractSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


logging.basicConfig(filename='epic_logging.log', encoding='utf-8',
                    level=logging.INFO)


class ContractViewset(ModelViewSet):
    serializer_class = ContractSerializer

    def get_queryset(self, *args, **kwargs):
        return Contract.objects.all()