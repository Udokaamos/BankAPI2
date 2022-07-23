from rest_framework import serializers
# from django.contrib.auth import get_user_model
# from rest_framework.exceptions import ValidationError
from .models import Deposit, Transfer, Withdraw



class DepositSerializer(serializers.ModelSerializer):
    deposit_amount = serializers.FloatField()
    class Meta:
        model = Deposit
        fields = ['id', 'deposit_amount', 'date_added']  


class TransferSerializer(serializers.ModelSerializer):
    recipient_name = serializers.CharField(max_length=100)
    recipient_acc_num = serializers.FloatField()
    trans_amount = serializers.FloatField()
    class Meta:
        model = Transfer
        fields = ['trans_amount','recipient_acc_num','recipient_name']


class WithdrawSerializer(serializers.ModelSerializer):
    withdrawal_amount = serializers.FloatField()
    class Meta:
        model = Withdraw
        fields =  ['withdrawal_amount']