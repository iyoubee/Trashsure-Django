# Generated by Django 4.1 on 2022-10-25 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prize', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redeemedprize',
            name='nama',
            field=models.TextField(),
        ),
    ]