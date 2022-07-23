# import random
# from typing_extensions import Self
# from unicodedata import name
from rest_framework.response import Response
from rest_framework import status 
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from account.models import User
from .serializers import  WithdrawSerializer, TransferSerializer, DepositSerializer
from account.serializers import UserSerializer
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
# from django.contrib.auth import authenticate
# from django.forms import model_to_dict
# from rest_framework.exceptions import ValidationError
from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated, IsAdminUser



User = get_user_model()

    

@swagger_auto_schema(methods=['POST'] ,
                    request_body=DepositSerializer())
@api_view([ 'POST'])
@authentication_classes([BasicAuthentication])
def deposit(request, user_id):


    if request.method == "POST":

        for user in User.objects.all():
            if user.id == user_id:
                user_data = {
                    'account_balance': request.data['deposit_amount'] + user.account_balance,
                    'id': user_id,
                    'email': user.email,
                    'phone': user.phone,
                    'password': user.password
                    
                }

                deposit_data = {
                    'deposit_amount': request.data['deposit_amount'],
                    'id': user_id
                }

                
                user_serializer = UserSerializer(instance=user, data=user_data)
                deposit_serializer = DepositSerializer(instance=user, data=deposit_data)
                if user_serializer.is_valid():
    
                #Allows user to signup or create account

                
                    if deposit_serializer.is_valid(): #validate the data that was passed
                        deposit_serializer.validated_data.update={
                            'account_balance'
                            }
                        
            
                        deposit_serializer.save(),
                        user_serializer.save()
                        data = {
                            'message' : 'success',
                            'data'  : deposit_serializer.data
                        }
                        
                        return Response(data, status=status.HTTP_201_CREATED)
                    else:
                        data = {
                            'message' : 'failed',
                            'error'  : deposit_serializer.errors
                        }
                        return Response(data, status=status.HTTP_400_BAD_REQUEST)



@swagger_auto_schema(methods=['POST'] ,
                    request_body=TransferSerializer())
@api_view(['POST'])
def transfers(request, user_id):

    if request.method == "POST":
        for user in User.objects.all():
            if user.id == user_id:
                user_data = {
                    'account_balance': user.account_balance - request.data['trans_amount'],
                    'id': user_id,
                    'email': user.email,
                    'phone': user.phone,
                    'password': user.password
                }

                transfer_data = {
                    'recipient_name': request.data['recipient_name'],
                    'recipient_acc_num': request.data['recipient_acc_num'],
                    'trans_amount': request.data['trans_amount'],
                    'id': user_id
                }
            
                user_serializer = UserSerializer(instance=user, data=user_data)
        
                transfer_serializer = TransferSerializer(instance=user, data=transfer_data)
                if user_serializer.is_valid():
                    
                    if transfer_serializer.is_valid():   
                        if  user.account_balance >= request.data['trans_amount']: 
                            transfer_serializer.save(),
                            user_serializer.save()
                            data = {
                                'message' : 'Transfer Successful',
                                'data'  : transfer_serializer.data
                                
                            }
                            return Response(data, status=status.HTTP_202_ACCEPTED)
        
                            
                        elif request.data['trans_amount'] > user.account_balance:
                            data = {
                                'message' : 'failed',
                                'error'  : 'Transfer amount must not be greater than the ledger balance.'
                            }
                            return Response(data, status=status.HTTP_403_FORBIDDEN)

                        
                    else:
                        data = {
                            'message' : 'failed',
                            'error'  : transfer_serializer.errors
                            
                        }
                        return Response(data, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods=['POST'] ,
                    request_body=WithdrawSerializer())
@api_view(['POST'])
def withdrawal(request, user_id):
    
    
    if request.method == 'POST':
    
        for user in User.objects.all():
            if user.id == user_id:
                user_data = {
                    'account_balance': user.account_balance - request.data['withdrawal_amount'],
                    'id': user_id,
                    'email': user.email,
                    'phone': user.phone,
                    'password': user.password

                }

                withdrawal_data = {
                    'withdrawal_amount': request.data['withdrawal_amount'],
                    'id': user_id
                }

                
                user_serializer = UserSerializer(instance=user, data=user_data)
                withdrawal_serializer = WithdrawSerializer(instance=user, data=withdrawal_data)
                if user_serializer.is_valid():
                    
                    if withdrawal_serializer.is_valid(): 
                        # withdrawal_serializer.save()
                        if user.account_balance >= request.data['withdrawal_amount']:  
                            withdrawal_serializer.save(),
                            user_serializer.save()
                            data = {
                                'message' : 'successful withdrawal',
                                'data'  : withdrawal_serializer.data
                            }
                            return Response(data, status=status.HTTP_200_OK)
                        
                     

                        elif request.data['withdrawal_amount'] > user.account_balance:
                            data = {
                                'message' : 'failed',
                                'error'  :  f' Insufficient funds!!'
                            }
                            return Response(data, status=status.HTTP_403_FORBIDDEN)

                    else:
                        data = {
                            'message' : 'failed',
                            'error'  : withdrawal_serializer.errors
                        }
                        return Response(data, status=status.HTTP_400_BAD_REQUEST)
