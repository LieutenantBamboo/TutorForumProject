# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 19:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20170307_1538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='pvotes',
            new_name='upvotes',
        ),
        migrations.RemoveField(
            model_name='questionpost',
            name='slug',
        ),
    ]