from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('store_manager.apps.authentication.urls', namespace='authentication'))
]
