from django.urls import path
from . import views



urlpatterns = [
    
    path('transactions/deposit/<int:user_id>', views.deposit, name="deposit"),
    path('transactions/transfer/<int:user_id>', views.transfers, name="transfers"),
    path('transactions/withdraw/<int:user_id>', views.withdrawal, name="withdrawals"), 

]