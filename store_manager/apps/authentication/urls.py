from django.urls import path

from .views import (
    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView)


app_name = 'authentication'

urlpatterns = [
    path('staff', UserRetrieveUpdateAPIView.as_view(),name='current_staff'),
    path('staff/create', RegistrationAPIView.as_view(), name='register'),
    path('staff/login/', LoginAPIView.as_view(), name='login'),
]