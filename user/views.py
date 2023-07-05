from datetime import datetime

from django.db.models import Sum, Max
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer, UserCreateSerializer, TopTotalTransactionSumSerializer, \
    TopMaxTransactionSerializer, UserUpdateSerializer

from dateutil.relativedelta import relativedelta


class ListUserView(ListCreateAPIView):
    """Class for viewing and creating users"""

    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializer
        elif self.request.method == 'POST':
            return UserCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            User.objects.create_user(
                email=serializer.data.get('email'),
                password=serializer.data.get('password')
            )
            return Response(request.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailUserView(RetrieveUpdateDestroyAPIView):
    """Class for updating and deleting users"""

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return UserUpdateSerializer
        else:
            return UserSerializer


class TopMaxTransactionUsersView(ListAPIView):
    """Class for viewing top-10 users with max transactions"""

    serializer_class = TopMaxTransactionSerializer

    def get_queryset(self):
        last_six_months = datetime.now() - relativedelta(months=6)
        queryset = User.objects. \
                       annotate(max_transaction=Max('transactions__sum')). \
                       filter(transactions__created_at__gte=last_six_months). \
                       order_by('-max_transaction')[:10]
        return queryset


class TopSumTransactionUsersView(ListAPIView):
    """Class for viewing top-10 users with total sum transactions"""

    serializer_class = TopTotalTransactionSumSerializer

    def get_queryset(self):
        last_six_months = datetime.now() - relativedelta(months=6)
        queryset = User.objects. \
                       annotate(total_transaction_sum=Sum('transactions__sum')). \
                       filter(transactions__created_at__gte=last_six_months). \
                       order_by('-total_transaction_sum')[:10]
        return queryset
