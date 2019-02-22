from django.test import TestCase
from django.utils.text import slugify

from .factories import CategoryFactory, ProductFactory
from .models import Category, Product


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
