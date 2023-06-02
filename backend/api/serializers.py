from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Transaction, Credit, Debit, Statement, Customer
from django.db import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import APIException
import random


class TransactionSerializer(serializers.ModelSerializer):

    # children = childcategory(many = True, read_only = True)

    # busines_email = serializers.EmailField(source='user.email', write_only = True)

    # kids = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # url = serializers.URLField()
    # time = serializers.SerializerMethodField(method_name='get_date_timestamp')

    # def get_date_timestamp(self, instance):
    #       return instance.time.timestamp() if instance.time else instance.time

    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ['balance']
        # exclude = ['id']


class StatementSerializer(serializers.ModelSerializer):

    

    class Meta:
        model = Statement
        fields = '__all__'
        read_only_fields = ['balance']
        # exclude = ['id']




