# Generated by Django 5.0.1 on 2024-03-01 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0012_alter_auction_time_ending'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='expired',
            field=models.BooleanField(default=False),
        ),
    ]
