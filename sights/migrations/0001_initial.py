# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 15:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hikers', '0001_initial'),
        ('hikes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('sight_type', models.CharField(
                    choices=[(b'0view', 'View'),
                             (b'1wildlife', 'Wildlife'),
                             (b'2flora', 'Plants')], max_length=10)),
                ('description', models.TextField()),
                ('best_time', models.CharField(
                    choices=[(b'0sunrise', 'Sunrise'),
                             (b'1morning', 'Morning'),
                             (b'2midday', 'Midday'),
                             (b'3evening', 'Early Evening'),
                             (b'4sunset', 'Sunset'),
                             (b'5dark', 'After Dark')],
                    max_length=10)),
                ('best_season', models.CharField(
                    choices=[(b'3winter', 'Winter'),
                             (b'0spring', 'Spring'),
                             (b'1summer', 'Summer'),
                             (b'2fall', 'Fall')], max_length=8)),
                ('added_by', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='sights_added', to='hikers.Hiker')),
                ('hike', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='sights', to='hikes.Hike')),
            ],
            options={
                'ordering': ['sight_type', 'best_season',
                             'best_time', '-modified'],
            },
        ),
    ]
