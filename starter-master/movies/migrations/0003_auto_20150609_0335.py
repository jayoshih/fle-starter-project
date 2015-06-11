# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_releasedate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='recommendation',
            name='from_user',
            field=models.ForeignKey(related_name='sender_name', to='movies.User'),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='movie',
            field=models.ForeignKey(to='movies.Movie'),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='to_user',
            field=models.ForeignKey(related_name='receiver_name', to='movies.User'),
        ),
    ]
