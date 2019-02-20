import factory

from factory import DjangoModelFactory, Faker

from .models import Category, Product


class CategoryFactory(factory.DjangoModelFactory):
    title = factory.Faker('name')
    description = factory.Faker('text')

    class Meta:
        model = Category


class ProductFactory(factory.DjangoModelFactory):

    class Meta:
        model = Product

    name = "product"
    category = factory.SubFactory(CategoryFactory)
    description = "description"
    quantity = 2
    price = 200.00
    deleted = False
