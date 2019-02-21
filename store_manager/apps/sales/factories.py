import factory

from django.conf import settings

from .models import Category, Product, SaleItem


class CategoryFactory(factory.DjangoModelFactory):

    class Meta:
        model = Category

    title = "Paper Things"
    description = "a long statement"


class ProductFactory(factory.DjangoModelFactory):

    class Meta:
        model = Product

    name = "product"
    category = factory.SubFactory(CategoryFactory)
    description = "description"
    quantity = 2
    price = 200.00
    deleted = False

class SaleItemFactory(factory.DjangoModelFactory):

    class Meta:
        model = SaleItem

    sale = factory.SubFactory(SaleFActory)
    product = factory.SubFactory(ProductFactory)
    product_title = "prroduct1"
    quantity = 2
