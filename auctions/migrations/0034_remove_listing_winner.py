# Generated by Django 3.1 on 2020-10-18 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0033_listing_winner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='winner',
        ),
    ]
