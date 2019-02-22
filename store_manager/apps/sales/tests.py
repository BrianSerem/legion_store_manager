from django.test import TestCase

# Create your tests here.
from .models import Category
from .factories import CategoryFactory

class CategoryModelTest(TestCase):
    def test_add_category(self):
        the_category= CategoryFactory()
        self.assertEqual(len(Category.objects.all()),1)
        self.assertTrue(isinstance(the_category.title, str))
        self.assertTrue(isinstance(the_category.description, str))
        self.assertTrue(len(the_category.title)>1)
        self.assertTrue(len(the_category.description)>1)
        the_category2 = CategoryFactory()
        self.assertEqual(len(Category.objects.all()),2)


        