# Generated by Django 4.1 on 2022-10-22 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deposit', '0004_pendingdeposit_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PendingDeposit',
        ),
    ]