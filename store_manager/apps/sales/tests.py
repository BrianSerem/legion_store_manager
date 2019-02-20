from django.test import TestCase

from .factories import (CategoryFactory, ProductFactory, SaleFactory,
                        SaleItemFactory, UserFactory)


# Create your tests here.

class SaleModelTests(TestCase):

    def setUp(self):
        self._category1 = CategoryFactory.create()
        self._product1 = ProductFactory.create(category=self._category1)
        self._user = UserFactory.create()
        self._sale = SaleFactory.create(attendant=self._user)

    def test_owner_can_add_attendant_to_sale(self):
        sale_test = SaleFactory.create(attendant=self._user)
        self.assertEqual(sale_test.attendant, self._user)

        