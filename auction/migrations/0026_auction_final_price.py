# Generated by Django 5.0.1 on 2024-03-23 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0025_rename_auction_id_bid_auction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='final_price',
            field=models.FloatField(null=True),
        ),
    ]
