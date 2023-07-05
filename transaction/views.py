from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.views import APIView

from transaction.models import Transaction
from transaction.serializers import TransactionSerializer, TransactionCreateSerializer


class ListTransactionView(ListCreateAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TransactionSerializer
        elif self.request.method == 'POST':
            return TransactionCreateSerializer


class DetailTransactionView(RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return TransactionCreateSerializer
        else:
            return TransactionSerializer
