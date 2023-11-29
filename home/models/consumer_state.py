from django.db import models
from home.models import Trader
from django.utils import timezone


class ConsumerState(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    consumer = models.OneToOneField(
        Trader, on_delete=models.CASCADE, related_name='consumer_state', unique=True
    )
    starting_balance = models.FloatField()
    balance_update = models.DateTimeField(auto_now_add=True, null=True)
    starting_equity = models.FloatField()
    can_trade = models.BooleanField(default=True)

    class Meta:
        db_table = 'consumer_state'
