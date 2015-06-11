# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReleaseDate',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('theater', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('movie', models.ForeignKey(to='movies.Movie')),
            ],
        ),
    ]
