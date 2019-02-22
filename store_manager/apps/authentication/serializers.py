import re
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .backends import generate_jwt_token


from django.contrib.auth.tokens import default_token_generator
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    # Serializers registration requests and creates a new user.ß


    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(
            User.objects.all(), 'That email is already used. '
            'Sign in instead or try another')]
    )
    role = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )
    username = serializers.CharField(
        validators=[UniqueValidator(
            User.objects.all(), 'That username is taken. Please try another')]
    )
    class Meta:
        # RegistrationSerializer uses User model
        model = User
        fields = ['email','role','username', 'password']

    def validate(self, data):
        password = data.get('password', None)
        if not re.match(r'^(?=.*[a-zA-Z])(?=.*[0-9]).*', password):
            raise serializers.ValidationError(
                'Invalid password. Please choose a password with at least a '
                'letter and a number.'
            )

        return data

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        return User.objects.create_user(**validated_data)

    def __init__(self, *args, **kwargs):
        super(RegistrationSerializer, self).__init__(*args, **kwargs)

        # Override the error_messages of each field with a custom error message
        for field in self.fields:
            field_error_messages = self.fields[field].error_messages
            field_error_messages['null'] = field_error_messages['blank'] \
                = field_error_messages['required'] \
                = 'Please fill in the {}'.format(field)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        email, password = data.get('email', None), data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if not password:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )
        user = authenticate(username=email, password=password)

        if not user:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )
        token = generate_jwt_token(email)
        return {
            'email': user.email,
            'username': user.username,
            'token': token

        }


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )


    class Meta:
        model = User
        fields = ('id','email', 'username','role', 'password')

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        for (key, value) in profile_data.items():
            setattr(instance.profile, key, value)

        if password is not None:
            instance.set_password(password)
        instance.save()

        # Save the user profile data
        instance.profile.save()
 
        return instance