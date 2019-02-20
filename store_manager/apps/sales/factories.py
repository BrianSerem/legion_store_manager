import factory
from factory import DjangoModelFactory, Faker

from .models import Category
from .models import Product


class CategoryFactory(DjangoModelFactory):
    title = factory.sequence(lambda x: f"category {x}")
    category_description = 'This category holds washing soaps'

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
