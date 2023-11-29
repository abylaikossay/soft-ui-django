from django.db import models


# Create your models here.
class Trader(models.Model):
    AGGRESSIVE = 'AGGRESSIVE'
    BALANCED = 'BALANCED'
    CONSERVATIVE = 'CONSERVATIVE'

    TRADER_TYPE = [
        (AGGRESSIVE, 'AGGRESSIVE'),
        (BALANCED, 'BALANCED'),
        (CONSERVATIVE, 'CONSERVATIVE'),
    ]
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    server = models.CharField(max_length=45)
    is_consumer = models.BooleanField(default=False)
    terminal_id = models.CharField(null=True, blank=True, max_length=45)
    trader_type = models.CharField(
        max_length=255, choices=TRADER_TYPE, default=BALANCED
    )
    trader_uid = models.CharField(max_length=45, null=True, blank=True)
    is_taken = models.BooleanField(default=False)
    coefficient = models.FloatField(default=1.0)
    balance = models.FloatField(default=0.0)
    equity = models.FloatField(default=0.0)

    class Meta:
        # Set the table name to match the existing 'traders' table in your PostgreSQL database
        db_table = 'traders'

    def __str__(self) -> str:
        return self.login + ' ' + self.server
