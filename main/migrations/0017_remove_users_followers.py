# Generated by Django 2.2.6 on 2020-05-04 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20200504_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='followers',
        ),
    ]