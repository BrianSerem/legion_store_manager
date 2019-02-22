import factory

from .models import Category

class CategoryFactory(factory.DjangoModelFactory):
    title = factory.Faker('name')
    description = factory.Faker('text')

    class Meta:
        model = Category