from rest_framework.response import Response
from rest_framework import generics

from .models import Transaction, Credit, Debit, Statement, Customer
from .serializers import TransactionSerializer, StatementSerializer

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.db.models import Count, Avg, Q

from rest_framework import permissions
import random
import datetime

# from django_filters import rest_framework as filters

class ApiItemPermission(permissions.BasePermission):

    # edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):

        return 1

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(not obj.api_id)



class AllTransactions(generics.ListCreateAPIView):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    # permission_classes = (IsAdminUser,)


class TransactionDetails(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = TransactionSerializer
    lookup_url_kwarg = 'account_number'
    lookup_field = 'account_number'
    queryset = Transaction.objects.all()
    # permission_classes = (ApiItemPermission,)

class GenerateStatement(generics.ListCreateAPIView):

    serializer_class = StatementSerializer
    queryset = Statement.objects.all()


class StatementDetail(generics.ListCreateAPIView):

    serializer_class = StatementSerializer
    lookup_url_kwarg = 'statement_id'
    lookup_field = 'id'
    queryset = Statement.objects.all()