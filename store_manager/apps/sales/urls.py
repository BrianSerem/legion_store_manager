from django.urls import path

from . import views


app_name = 'sales'

urlpatterns = [
    path('products', views.ProductListCreateAPIView.as_view(),
         name='list_create_product'),
]
