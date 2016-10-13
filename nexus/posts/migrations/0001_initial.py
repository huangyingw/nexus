# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 16:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hubs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.SlugField(blank=True, default='', max_length=256)),
                ('slug', models.SlugField(default='', max_length=256)),
                ('pub_date', models.DateTimeField(blank=True)),
                ('body', models.TextField(blank=True, default='', null=True)),
                ('score', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('wordcount', models.IntegerField(default=0)),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('hubs', models.ManyToManyField(blank=True, related_name='posts', to='hubs.Hub')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='posts.Post')),
                ('repost', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reposts', to='posts.Post')),
            ],
        ),
    ]
