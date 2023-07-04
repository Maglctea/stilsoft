from rest_framework.serializers import ModelSerializer

from user.models import User, Balance


class BalanceSerializer(ModelSerializer):
    class Meta:
        model = Balance
        fields = '__all__'


class UserSerializer(ModelSerializer):
    balance = BalanceSerializer()

    class Meta:
        model = User
        fields = '__all__'
