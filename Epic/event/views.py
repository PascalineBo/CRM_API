import logging

from django.shortcuts import render
from rest_framework import status, exceptions
from rest_framework.permissions import IsAuthenticated
from .models import Event
from .serializers import EventSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth import get_user_model


logging.basicConfig(filename='epic_logging.log', encoding='utf-8',
                    level=logging.INFO)


class EventViewset(ModelViewSet):
    serializer_class = EventSerializer


    def get_queryset(self):
        return Event.objects.all()

