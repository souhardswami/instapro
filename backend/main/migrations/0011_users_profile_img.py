# Generated by Django 2.2.6 on 2020-04-30 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200420_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='profile_img',
            field=models.ImageField(null=True, upload_to='pics/'),
        ),
    ]