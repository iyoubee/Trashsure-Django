# Generated by Django 4.1 on 2022-10-21 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposit', '0003_alter_pendingdeposit_beratsampah_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pendingdeposit',
            name='username',
            field=models.TextField(default=''),
        ),
    ]
