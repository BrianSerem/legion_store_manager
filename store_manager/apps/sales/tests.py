from django.test import TestCase
from django.utils.text import slugify

from .factories import CategoryFactory, ProductFactory
from .models import Product

class CategoryModelTests(TestCase):

    def setUp(self):
        self._category = CategoryFactory.create()

    def test_category_string_representation(self):
        self.assertEqual(str(self._category), self._category.title)

    def test_generating_slugs_from_title(self):
        category = CategoryFactory.create()
        self.assertEqual(category.slug, slugify(category.title))
        category.title = "onother thing"
        category.save()
        self.assertNotEqual(category.slug, slugify(category.title))
        

class ProductModelTests(TestCase):

    def setUp(self):
        self._category1 = CategoryFactory.create()
        self._product1 = ProductFactory.create(category=self._category1)

    def test_product_string_represenation(self):
        self.assertEqual(str(self._product1), self._product1.name)
        

class ProductQuerysetsTests(TestCase):

    def setUp(self):
        self._category1 = CategoryFactory.create()

    def test_products_queryset_returns_active_products(self):
        product1 = ProductFactory.create(category=self._category1)
        product2 = ProductFactory.create(category=self._category1)
        product3 = ProductFactory.create(category=self._category1)
        product2.deleted = True
        product2.save()

        self.assertQuerysetEqual(
            Product.products.active(),
            [repr(product) for product in  Product.objects.filter(deleted=False)]
        )
