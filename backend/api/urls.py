from django.urls import path

from .views import AllTransactions, TransactionDetails, GenerateStatement, StatementDetail
urlpatterns = [ 

    path('transactions', AllTransactions.as_view(), name = 'all-transactions'),
    path('statements', GenerateStatement.as_view(), name = 'statements'),

    path('statements/<statement_id>', StatementDetail.as_view(), name = 'statement-detail'),
    path('transactions/<transaction_id>', TransactionDetails.as_view(), name = 'transaction-detail'),

        ]

