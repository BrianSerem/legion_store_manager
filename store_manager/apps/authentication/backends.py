import jwt
import datetime

from django.conf import settings
from rest_framework import authentication, exceptions

from .models import User


def generate_jwt_token(username):
    """
    This method generates a jwt string with username encoded in it.
    """
    time = datetime.datetime.utcnow() + datetime.timedelta(hours=12)
    token = jwt.encode({
        "username": username,
        "exp": time,
    }, settings.SECRET_KEY, algorithm='HS256')

    return token.decode('utf-8')


class JWTAuthentication(authentication.TokenAuthentication):
   
    keyword = 'Bearer'

    def authenticate_credentials(self, token):
       
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            try:
                user = User.objects.get(username=payload['username'])
                return user, None
            except User.DoesNotExist:
                return None, None
        except jwt.exceptions.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Expired Token.')
        except jwt.exceptions.InvalidTokenError:
            raise exceptions.AuthenticationFailed('Invalid token you guys')