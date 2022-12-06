import logging

from rest_framework.response import Response
from authentication.serializers import UserSerializer
from rest_framework import status
from .models import User
from rest_framework.viewsets import ModelViewSet
from .permissions import IsControlling
from rest_framework.permissions import IsAuthenticated


logging.basicConfig(filename='epic_logging.log', encoding='utf-8',
                    level=logging.INFO)


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    permission_classes = [IsAuthenticated & IsControlling]

    def get_queryset(self):
        return User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'user': UserSerializer(user,
                                       context=self.get_serializer_context()
                                       ).data,
                'message': "User created successfully."},
                status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
