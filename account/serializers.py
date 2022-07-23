from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from account.models import User

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 255, write_only=True)
    account_balance = serializers.ReadOnlyField()
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['id','first_name', 'last_name','account_num', 'account_balance', 'email', 'password', 'phone','branch','bank_name','date_created']


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)

