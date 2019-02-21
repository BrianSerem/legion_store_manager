import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, role=None):
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email), role = role)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password,  role = "admin"):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, role, password)
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    role = models.CharField(db_index=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        
        return self.username

    def get_short_name(self):
       
        return self.username


