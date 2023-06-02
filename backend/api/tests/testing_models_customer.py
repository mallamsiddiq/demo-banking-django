from django.test import TestCase
from api.models import Transaction, Credit, Debit, Statement, Customer
# from model_bakery import baker
# from pprint import pprint


class TestItemModel(TestCase):

    @classmethod
    def setUpTestData(cls):

        user1 = Customer.objects.create(
            name = 'adubi',
            account_number = 123456,
            balance = 100)

    def test_red_str(self):
        self.assertTrue(1)
    