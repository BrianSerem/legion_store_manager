from rest_framework import status, generics
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    LoginSerializer, RegistrationSerializer, UserSerializer)



class RegistrationAPIView(generics.CreateAPIView):
    

    serializer_class = RegistrationSerializer

    def post(self, request):
        # Separate requests
        email, username, role, password = request.data.get(
            'email', None), request.data.get('username', None),request.data.get('role',None),request.data.get('password', None)

        user = {"email": email, "username": username, "role":role, "password": password}
      
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(data, status=status.HTTP_201_CREATED)

    def get(self, request):
        return Response(
            data={
                "message": 'Only post requests are allowed to this endpoint.'
            })


class LoginAPIView(generics.GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
        email, password = request.data.get('email', None), request.data.get(
            'password', None)

        user = {"email": email, "password": password}
    
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.data

        return Response(user_data, status=status.HTTP_200_OK)

    def get(self, request):
        return Response(
            data={
                "message": 'Only post requests are allowed to this endpoint.'
            })


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
   
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
       
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})
        serializer_data = {
            'username': serializer_data.get('username', request.user.username),
            'email': serializer_data.get('email', request.user.email)
        }

        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
