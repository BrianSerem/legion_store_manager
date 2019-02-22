import factory

from django.conf import settings

from .models import Product, Sale, SaleItem, Category


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


class UserFactory(factory.DjangoModelFactory):

    class Meta:
        model = settings.AUTH_USER_MODEL

    username = factory.sequence(lambda x: "User %d" % x)
    email = factory.sequence(lambda x: "email%d@email.com" % x)


class SaleFactory(factory.DjangoModelFactory):

    class Meta:
        model = Sale

    attendant = factory.SubFactory(UserFactory)


class SaleItemFactory(factory.DjangoModelFactory):

    class Meta:
        model = SaleItem

    sale = factory.SubFactory(SaleFactory)
    product = factory.SubFactory(ProductFactory)
    product_title = "prroduct1"
    quantity = 2
