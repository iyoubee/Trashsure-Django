# Generated by Django 4.1 on 2022-10-21 09:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('withdraw', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pendingwithdraw',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]