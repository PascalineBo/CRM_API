from django.shortcuts import render
from rest_framework.response import Response
from authentication.serializers import UserSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import status

# Create your views here.
class RegisterAPIView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
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