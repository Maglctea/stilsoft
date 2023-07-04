from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView

from transaction.models import Transaction
from transaction.serializers import TransactionSerializer, TransactionCreateSerializer


class ListTransactionView(ListAPIView, CreateAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TransactionSerializer
        elif self.request.method == 'POST':
            return TransactionCreateSerializer
