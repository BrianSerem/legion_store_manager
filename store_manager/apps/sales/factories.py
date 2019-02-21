from factory import DjangoModelFactory, Faker

from .models import Category

class CategoryFactory(DjangoModelFactory):
    title = Faker('Detergent')
    category_description = Faker('This category holds washing soaps')

    class Meta:
        model = Category