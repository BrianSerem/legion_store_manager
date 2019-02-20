from django.test import TestCase
from django.utils.text import slugify

from .models import Category, Product
from .factories import CategoryFactory, ProductFactory


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

        category = CategoryFactory.create()
        self.assertEqual(str(category), category.title)

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
