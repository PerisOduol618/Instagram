# Generated by Django 2.2.8 on 2020-10-21 22:22

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0004_auto_20201022_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(blank=True, default=None, verbose_name=django.contrib.auth.models.User),
        ),
    ]