# Generated by Django 4.1.12 on 2023-11-29 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_consumerstate_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumerstate',
            name='balance_update',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]