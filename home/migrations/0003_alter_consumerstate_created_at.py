# Generated by Django 4.1.12 on 2023-11-29 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_originalposition_consumerstate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumerstate',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
