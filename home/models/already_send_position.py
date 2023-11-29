from django.db import models
from django.utils import timezone


class AlreadySentPosition(models.Model):
    id = models.BigAutoField(primary_key=True)
    ticket = models.BigIntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    trader_name = models.CharField(max_length=255)
    server = models.CharField(max_length=255)

    class Meta:
        db_table = 'already_send_positions'
