# Generated by Django 3.0.6 on 2020-06-04 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_products_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
    ]
