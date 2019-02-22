from django.urls import path

from .views import (
    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView,UsersRetrieveApiView, SingleUserRetrieveApiView,DeleteUserApiView
)

app_name = 'authentication'

urlpatterns = [
    path('staff/', UsersRetrieveApiView.as_view(),name='staff'),
    path('staff/create', RegistrationAPIView.as_view(), name='register'),
    path('staff/login', LoginAPIView.as_view(), name='login'),
    path('staff/<pk>', SingleUserRetrieveApiView.as_view(),name='single-staff'),
    path('staff/<pk>/delete', DeleteUserApiView.as_view(),name='delete-staff'),

]