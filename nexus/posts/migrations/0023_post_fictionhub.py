# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-31 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0022_post_wordcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fictionhub',
            field=models.BooleanField(default=False),
        ),
    ]