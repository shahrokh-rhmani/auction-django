# Generated by Django 5.0.1 on 2024-03-17 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0019_remove_product_date_posted_remove_product_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='country',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='post_code',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='town',
        ),
    ]
