# Generated by Django 4.2.5 on 2023-10-09 18:03

import backend.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_favoritebarter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostName', models.CharField(default='', max_length=200)),
                ('productTitle', models.CharField(default='', max_length=200)),
                ('basePrice', models.CharField(default='', max_length=100)),
                ('minimumBid', models.CharField(default='', max_length=100)),
                ('auctionDate', models.DateField()),
                ('auctionTime', models.DateTimeField()),
                ('auctionDescription', models.CharField(default='', max_length=2000000)),
                ('auctionLocation', models.CharField(default='', max_length=200)),
                ('auctionAddress', models.CharField(default='', max_length=10000)),
                ('productImage', backend.models.FileField(blank=True, default='', upload_to='AuctionImages/')),
            ],
        ),
    ]