from django.test import TestCase

from .factories import CategoryFactory, ProductFactory


class CategoryModelTests(TestCase):

    def setUp(self):
        self._category = CategoryFactory.create()

    def test_category_string_representation(self):
        self.assertEqual(str(self._category), self._category.title)


class ProductModelTests(TestCase):

    def setUp(self):
        self._category1 = CategoryFactory.create()
        self._product1 = ProductFactory.create(category=self._category1)

    def test_product_string_represenation(self):
        self.assertEqual(str(self._product1), self._product1.name)
