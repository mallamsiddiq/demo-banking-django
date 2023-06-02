from django.contrib import admin

from .models import Transaction, Credit, Debit, Statement, Customer


for model in (Transaction, Credit, Debit, Statement, Customer):

	admin.site.register(model)


# Register your models here.
