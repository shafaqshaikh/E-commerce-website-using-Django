# Generated by Django 3.0.6 on 2020-06-04 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_order_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='tags',
            field=models.ManyToManyField(to='accounts.Tag'),
        ),
    ]