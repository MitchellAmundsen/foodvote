# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-06-10 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodvote', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='location',
            field=models.TextField(default=b'seattle'),
        ),
    ]