# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.CharField(unique=True, primary_key=True, max_length=200, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AlternateID',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('actor', models.ForeignKey(to='movies.Actor')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.CharField(unique=True, primary_key=True, max_length=200, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('year', models.DateField()),
                ('mpaa_rating', models.CharField(max_length=100)),
                ('runtime', models.IntegerField(default=0)),
                ('synopsis', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=800)),
                ('movie', models.ForeignKey(to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('critics_rating', models.CharField(max_length=1000)),
                ('critics_score', models.IntegerField(default=0)),
                ('audience_score', models.IntegerField(default=0)),
                ('movie', models.ForeignKey(to='movies.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='movie',
            field=models.ForeignKey(to='movies.Movie'),
        ),
        migrations.AddField(
            model_name='alternateid',
            name='movie',
            field=models.ForeignKey(to='movies.Movie'),
        ),
    ]
