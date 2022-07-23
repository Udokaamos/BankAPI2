# from django.apps import AppConfig


# class TransactionsConfig(AppConfig):
#     name = 'transactions'
from django.contrib import admin
from .models import Deposit, Transfer, Withdraw
# from django.contrib.auth import get_song_view


# Register your models here
# Song = get_song_view()
admin.site.register(Deposit)
admin.site.register(Transfer)
admin.site.register(Withdraw)