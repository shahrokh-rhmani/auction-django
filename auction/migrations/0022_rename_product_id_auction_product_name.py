# Generated by Django 5.0.1 on 2024-03-20 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0021_alter_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='product_id',
            new_name='product_name',
        ),
    ]
