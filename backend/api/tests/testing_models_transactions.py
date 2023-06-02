from django.test import TestCase
from api.models import Transaction, Credit, Debit, Statement, Customer
import datetime
# from model_bakery import baker
# from pprint import pprint


class TestItemModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase 

        cls.user1 = Customer.objects.create(
            name = 'adubi',
            account_number = 123456,
            balance = 10000)

        cls.user2 = Customer.objects.create(
            name = 'asake',
            account_number = 523456,
            balance = 45000)

        cls.transaction1 = Credit.objects.create(
            customer_id = 1,

            # created_date = models.DateTimeField(auto_now_add=True)
            # effective_date = models.DateTimeField(default = datetime.date(2022,10,22))

            # checque_no = models.IntegerField(null = True)
            description = "a testing credit transaction",

            _amount = 223)

            #   saving balance here to be date trackable
            # balance = models.FloatField(default = 0))

        cls.transaction2 = Credit.objects.create(
            customer_id = 1,

            # created_date = models.DateTimeField(auto_now_add=True)
            # effective_date = models.DateTimeField(default = datetime.date(2022,10,22))

            # checque_no = models.IntegerField(null = True)
            description = "a testing credit transaction 2",

            _amount = 449)

        cls.transaction3 = Debit.objects.create(
            customer_id = 2,

            # created_date = models.DateTimeField(auto_now_add=True)
            # effective_date = models.DateTimeField(default = datetime.date(2022,10,22))

            # checque_no = models.IntegerField(null = True)
            description = "a testing debit transaction",

            _amount = 436)

        cls.statement1 = Statement.objects.create(customer_id = 1, 
            start_date = datetime.datetime(2022, 12, 14),
            end_date = datetime.datetime.now())

        cls.statement2 = Statement.objects.create(customer_id = 2, 
            start_date = datetime.datetime(2022, 12, 14),
            end_date = datetime.datetime.now())


        cls.user1 = Customer.objects.get( account_number = 123456)

        cls.user2 = Customer.objects.get( account_number = 523456)

    def test_credit_balance(self):
        self.assertEqual(self.transaction1.credit_amount, 223)

    def test_debit_balance(self):
        self.assertEqual(self.transaction3.debit_amount, 436)

    def test_wrong_gateway(self):

        with self.assertRaisesMessage(AttributeError, "'Debit' object has no attribute 'credit_amount'"):

            self.transaction3.credit_amount

        with self.assertRaises(AttributeError):

            self.transaction1.debit_amount

    def test_transaction_type(self):
        self.assertEqual(self.transaction1.type_, 'Credit')
        self.assertEqual(self.transaction2.type_, 'Credit')
        self.assertEqual(self.transaction3.type_, 'Debit')


    def test_customer_balance_after_credit1(self):
        self.assertEqual(self.transaction1.balance, 10000 + 223)

    def test_customer_balance_after_credit2(self):
        self.assertEqual(self.transaction2.balance, 10000 + 223 + 449)


    def test_customer_balance_after_debit1(self):
        self.assertEqual(self.transaction3.balance, 45000 - 436)

    def test_customer_balance_after_all(self):
        self.assertEqual(self.user1.balance, 10000 + 223 + 449)
        self.assertEqual(self.user2.balance, 45000 - 436)


    def test_statements(self):

        # for transaction in self.statement1.transactions:

        #     print(transaction.created_date)
        
        self.assertEqual(self.statement1.balance, 10000 + 223 + 449)
