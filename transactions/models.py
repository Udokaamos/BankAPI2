from django.db import models
from django.contrib.auth import get_user_model
from django.forms import model_to_dict
from account.models import User

User = get_user_model()


class Deposit(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="deposit")
    deposit_amount = models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.user


class Transfer(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient_name = models.CharField(max_length=50, blank=True)
    recipient_acc_num = models.FloatField()
    recipient_bank_name = models.CharField(max_length=50, blank=True)
    trans_amount = models.FloatField()
    
    def __str__(self) -> str:
         return f"{self.trans_amount}" # to {self.recipient_name}"
    

class Withdraw(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCAD)
    withdrawal_amount = models.FloatField()


    def __str__(self) -> str:
        return f"{self.withdrawal_amount}"