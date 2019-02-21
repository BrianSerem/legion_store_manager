import jwt
from rest_framework import status, generics
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings



from .serializers import (
    LoginSerializer, RegistrationSerializer, UserSerializer)

from .models import User


class RegistrationAPIView(generics.CreateAPIView):

    #permission_classes = (AllowAny)
    serializer_class = RegistrationSerializer


    def post(self, request):
        # Separate requests
        email, username, role, password = request.data.get(
            'email', None), request.data.get('username', None), request.data.get('role', None), request.data.get('password',None)

        user = {"email": email, "username": username, "password": password, "role": role}
        data = user
        serializer = self.serializer_class(data = user)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        success_message = {'message': 'Registration successful'}
        data.update(success_message)
        return Response(data, status=status.HTTP_201_CREATED)

    def get(self, request):
        return Response(
            data={
                "message": 'Only post requests are allowed to this endpoint.'
            })


class LoginAPIView(generics.GenericAPIView):
    #permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        email, password = request.data.get('email', None), request.data.get(
            'password', None)

        user = {"email": email, "password": password}

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.data

        user_data['token'] = generate_jwt_token(user_data['username'])

        return Response(user_data, status=status.HTTP_200_OK)

    def get(self, request):
        return Response(
            data={
                "message": 'Only post requests are allowed to this endpoint.'
            })


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    #permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):

        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})
        serializer_data = {
            'username': serializer_data.get('username', request.user.username),
            'email': serializer_data.get('email', request.user.email),
            'role': serializer_data.get('role', request.user.role)}

        # Here is that serialize, validate, save pattern we talked about before.
        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

class UsersRetrieveApiView(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer






        