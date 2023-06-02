import datetime
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .usermanager import UserManager

from django.db.models import Sum


class Customer(AbstractBaseUser, PermissionsMixin):

    #   USER
    name = models.CharField( max_length=40)
    account_number = models.IntegerField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    balance = models.FloatField()

    #   defaults
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'account_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):

        return f"Customer : {self.account_number}"


class Transaction(models.Model):

    customer = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name = 'transactions')

    created_date = models.DateTimeField(auto_now_add=True)
    effective_date = models.DateTimeField(default = datetime.date(2022,10,22))

    checque_no = models.IntegerField(null = True)
    description = models.CharField(max_length= 64)

    _amount = models.FloatField(default = 0)

    #   saving balance here to be date trackable
    balance = models.FloatField(default = 0)

    @property
    def type_(self):
        return self.__class__.__name__


    class Meta:
        # ordering = ['-created_date']
        get_latest_by = ["created_date", 'pk']

    def __str__(self):

        return f"transaction -- {self.description}"


class Credit(Transaction):

    @property
    def credit_amount(self):
        return self._amount

    def save(self, *args, **kwargs):
        current_balance = self.customer.balance + self._amount

        self.customer.balance = current_balance
        self.customer.save()
        self.balance = current_balance

        # kwargs |= {'balance' : self.}
        super(Credit, self).save(*args, **kwargs)


class Debit(Transaction):

    @property
    def debit_amount(self):
        return self._amount


    def save(self, *args, **kwargs):
        current_balance = self.customer.balance - self._amount
        self.customer.balance = current_balance
        self.customer.save()
        self.balance = current_balance
        # kwargs |= {'balance' : self.}
        super(Debit, self).save(*args, **kwargs)

#   If we would be saving an instance of the statements generated rather than just 
#   implementing it at the views/serialzers level then statements’ model is as follow


class Statement(models.Model):

    customer = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name = 'statements')
    date_generated = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    #   saving balance here to make it date-trackable
    balance = models.FloatField(default = 0) 

    @property
    def transactions(self):
        end_date = self.end_date + datetime.timedelta(days=1)
        return self.customer.transactions.filter(created_date__range=[self.start_date, end_date])


    def save(self, *args, **kwargs):

        if self.transactions.count():

            self.balance = self.transactions.latest().balance

        super(Statement, self).save(*args, **kwargs)