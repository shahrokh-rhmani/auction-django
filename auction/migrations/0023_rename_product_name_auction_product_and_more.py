# Generated by Django 5.0.1 on 2024-03-20 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0022_rename_product_id_auction_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='product_name',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='userdetails',
            old_name='user_id',
            new_name='user',
        ),
    ]
