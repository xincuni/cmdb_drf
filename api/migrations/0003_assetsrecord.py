# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-10-31 03:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_disk'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetsRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='内容')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Server', verbose_name='服务器')),
            ],
        ),
    ]
