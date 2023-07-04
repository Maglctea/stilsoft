from rest_framework import serializers
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


class UserCreateSerializer(ModelSerializer):

    password2 = serializers.CharField()
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2')
