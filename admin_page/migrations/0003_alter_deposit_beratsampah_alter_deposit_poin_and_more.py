# Generated by Django 4.1 on 2022-10-21 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_page', '0002_deposit_date_withdraw_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='beratSampah',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='poin',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='totalHarga',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='prize',
            name='poin',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='prize',
            name='stok',
            field=models.BigIntegerField(),
        ),
    ]
