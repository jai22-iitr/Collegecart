# Generated by Django 3.1.4 on 2021-04-06 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_item_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='views',
        ),
    ]
