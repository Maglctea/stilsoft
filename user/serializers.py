from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from django.utils.translation import gettext_lazy as _
from user.models import User, Balance


class BalanceSerializer(ModelSerializer):
    class Meta:
        model = Balance
        fields = '__all__'


class UserSerializer(ModelSerializer):
    balance = BalanceSerializer()

    class Meta:
        model = User
        fields = ('email', 'balance')


class TopMaxTransactionSerializer(ModelSerializer):
    balance = BalanceSerializer()
    max_transaction = serializers.CharField(max_length=15)

    class Meta:
        model = User
        fields = ('email', 'balance', 'max_transaction')


class TopTotalTransactionSumSerializer(ModelSerializer):
    balance = BalanceSerializer()
    total_transaction_sum = serializers.CharField(max_length=15)

    class Meta:
        model = User
        fields = ('email', 'balance', 'total_transaction_sum')


class UserCreateSerializer(ModelSerializer):

    def validate_email(self, value):
        try:
            validate_email(value)
            return value

        except ValidationError as e:
            raise serializers.ValidationError(e.message)

    def validate_password(self, value):
        try:
            if not value:
                raise ValidationError(_('The Password must be set'))
            return value

        except ValidationError as e:
            raise serializers.ValidationError(e.message)

    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {
            'email': {'required': True},
            'password': {'required': True}
        }
