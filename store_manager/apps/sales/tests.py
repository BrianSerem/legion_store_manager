from django.test import TestCase

# Create your tests here.
from .models import Category
from .factories import CategoryFactory

class CategoryTestCase(TestCase):
    def test_add_category(self):
        category2 = CategoryFactory.create()
        self.assertEqual(category2.title,'Detergent')

        