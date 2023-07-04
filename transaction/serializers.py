from rest_framework.serializers import ModelSerializer

from transaction.models import Transaction
from user.serializers import UserSerializer


class TransactionSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Transaction
        fields = '__all__'
