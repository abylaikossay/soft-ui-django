from django.db import models
from django.utils import timezone


class ProviderExistingPosition(models.Model):
    id = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=255)
    type = models.IntegerField()
    reason = models.IntegerField(null=True)
    created_at = models.DateTimeField(default=timezone.now, null=True)
    comment = models.CharField(max_length=255)
    trader_uid = models.CharField(max_length=255)
    server = models.CharField(max_length=255)
    volume = models.FloatField()
    price_open = models.FloatField()
    ticket = models.BigIntegerField()
    sl = models.FloatField(null=True)
    tp = models.FloatField(null=True)
    comission = models.FloatField(null=True)
    swap = models.FloatField(null=True)
    profit = models.FloatField(null=True)
    time = models.BigIntegerField()
    time_msc = models.BigIntegerField()
    time_update = models.BigIntegerField()
    time_update_msc = models.BigIntegerField()

    class Meta:
        db_table = 'provider_existing_positions'

    def __str__(self) -> str:
        return str(self.ticket) + ' ' + str(self.type)
