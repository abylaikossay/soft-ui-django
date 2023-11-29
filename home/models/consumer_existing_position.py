from django.db import models
from django.utils import timezone


class ConsumerExistingPosition(models.Model):
    id = models.BigAutoField(primary_key=True)
    ticket = models.BigIntegerField()
    created_at = models.DateTimeField(default=timezone.now, null=True)
    time_in = models.DateTimeField(null=True)
    type = models.CharField(max_length=255)
    volume_in = models.FloatField()
    symbol = models.CharField(max_length=255)
    price_in = models.FloatField()
    sl = models.FloatField(default=0.0, null=True)
    tp = models.FloatField(default=0.0, null=True)
    volume_out = models.FloatField(null=True)
    time_out = models.DateTimeField(null=True)
    price_out = models.FloatField(null=True)
    commission = models.FloatField(null=True)
    swap = models.FloatField(null=True)
    profit = models.FloatField(null=True)
    trader_name = models.CharField(max_length=255)
    is_closed = models.BooleanField(default=False, null=True)
    server = models.CharField(max_length=255)
    broker = models.CharField(max_length=255, null=True, blank=True)
    comment = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'consumer_existing_positions'

    def __str__(self) -> str:
        return str(self.ticket) + ' ' + self.type
