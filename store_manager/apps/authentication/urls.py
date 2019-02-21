from django.urls import path

from .views import (
    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView,UsersRetrieveApiView
)

app_name = 'authentication'

urlpatterns = [
    path('staff', UsersRetrieveApiView.as_view(),name='staff'),
    path('staff/create/', RegistrationAPIView.as_view(), name='register'),
    path('staff/login/', LoginAPIView.as_view(), name='login'),

]