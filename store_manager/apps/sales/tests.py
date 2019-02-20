from django.test import TestCase

from .models import Category, Product
from .factories import CategoryFactory, ProductFactory


class CategoryTestCase(TestCase):
    def test_add_category(self):
        category = CategoryFactory.create()
        self.assertEqual(str(category), category.title)


class ProductModelTests(TestCase):

    def setUp(self):
        self._category1 = CategoryFactory.create()
        self._product1 = ProductFactory.create(category=self._category1)

    def test_product_string_represenation(self):
        self.assertEqual(str(self._product1), self._product1.name)


class ProductManager(TestCase):
    
    def setUp(self):
        self._category1 = CategoryFactory.create()

    def test_products_active_queryset(self):
        product1 = ProductFactory.create(category=self._category1)
        product2 = ProductFactory.create(category=self._category1)
        product3 = ProductFactory.create(category=self._category1)

        product2.deleted = False
        product2.save()

        self.assertQuerysetEqual(
            Product.products.active(),
            [repr(product) for product in Product.objects.filter(deleted=False)]
        )
