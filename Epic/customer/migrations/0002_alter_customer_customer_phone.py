# Generated by Django 4.1.3 on 2022-11-24 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_phone',
            field=models.CharField(max_length=17),
        ),
    ]