# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-14 21:31
from __future__ import unicode_literals

from django.contrib.postgres.operations import HStoreExtension
from django.db import migrations, models
import django.contrib.postgres.fields.hstore
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_report_sla_triaged_at'),
    ]

    operations = [
        HStoreExtension(),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField()),
                ('attributes', django.contrib.postgres.fields.hstore.HStoreField(default=dict)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='dashboard.Report')),
            ],
            options={
                'verbose_name': 'activity',
                'verbose_name_plural': 'activities',
                'ordering': ['created_at'],
            },
        ),
    ]
