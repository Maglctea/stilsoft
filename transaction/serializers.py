from rest_framework.serializers import ModelSerializer

from transaction.models import Transaction
from user.serializers import UserSerializer


class TransactionSerializer(ModelSerializer):
    """Serializer for view transactions"""

    user = UserSerializer()

    class Meta:
        model = Transaction
        fields = '__all__'


class TransactionCreateSerializer(ModelSerializer):
    """Serializer for creating transactions"""

    class Meta:
        model = Transaction
        fields = ('user', 'type', 'sum')
