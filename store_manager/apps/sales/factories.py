from factory import DjangoModelFactory, Faker

from .models import Category

class CategoryFactory2(DjangoModelFactory):
    title = Faker('Detergent')
    category_description = Faker('This category holds washing soaps')

    class Meta:
        model = Category