from django.http import HttpResponse
from django.contrib.auth.models import AnonymousUser, User
from django.utils import timezone

# from tastypie.http import HttpUnauthorized, HttpForbidden, HttpBadRequest
from datetime import datetime, timedelta
from .models import AuthToken
from django.conf import settings
from django.contrib.auth.models import User
import logging
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from .exceptions import *

# """
# This is the custom authentication implementation using Authentication
# """

class CustomAuthentication(BaseAuthentication):

    def __init__(self, realm="API"):
        self.realm = realm

    def authenticate(self, request, **kwargs):
        """[Function to get the token from the header of the API calls made to the system\
         and override the deafult authentication provided by the Django to customise on out own.]
        Arguments:
            request {[type]} -- [description]
        Raises:
            ClientNotFound: [When Client is not registered with us]
            TokenExpired: [When the token is expired and the client tried to access the secured API]
        Returns:
            [token] -- [userobj]
        """
        try:
            # username = request.GET.get('HTTP_X_USERNAME')
            # print(username)
            auth_header_value = request.META.get("HTTP_AUTHORIZATION", "")
            print(auth_header_value)
            if auth_header_value:
                authmeth, auth = request.META["HTTP_AUTHORIZATION"].split(" ", 1)
                if not auth:
                    return None
                if not authmeth.lower() == "bearer":
                    return None
                token = CustomAuthentication.verify_access_token(request, auth)
                return (token, None)
            else:
                raise ClientNotFound()
        except TokenExpired as _e:
            raise TokenExpired()
        except KeyError as _e:
            request.user = AnonymousUser()
            raise ClientNotFound()

    @staticmethod
    def verify_access_token(username, auth):
        """[verify the token provided with the Auth Token table and retun a user object to \
        overide the default authentication]
        Arguments:
            request {[type]} -- [description]
            auth {[token]} -- [access token]
        Raises:
            ClientNotFound: [When Client is not registered with us]
            TokenExpired: [When the token is expired and the client tried to access the secured API]
        Returns:
            [user] -- [user obj]
        """
        AuthToken_ = AuthToken.objects.filter(access_token=auth)
        if AuthToken_.exists():
            token = AuthToken.access_token
            user = User.objects.get_or_create(username=token.user)[0]
            # print(user)
            if token.expiry_date < timezone.now():
                token.expired = True
                token.save()
                raise TokenExpired()
            return user
        else:
            raise ClientNotFound()