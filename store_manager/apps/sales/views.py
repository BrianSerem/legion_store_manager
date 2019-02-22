from rest_framework import generics
from rest_framework import permissions

from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.products.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductSerializer

    def create(self, *args, **kwargs):
        user = self.request.user
        super().create(*args, **kwargs)
