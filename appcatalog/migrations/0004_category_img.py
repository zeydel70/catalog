# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-28 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcatalog', '0003_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.ImageField(blank=True, help_text=b'category_image', upload_to=b'images'),
        ),
    ]
