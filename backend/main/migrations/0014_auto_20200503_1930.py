# Generated by Django 2.2.6 on 2020-05-03 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_users_followers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='image',
        ),
        migrations.AddField(
            model_name='photos',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Users'),
        ),
        migrations.AlterField(
            model_name='users',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='_users_followers_+', to='main.Users'),
        ),
    ]