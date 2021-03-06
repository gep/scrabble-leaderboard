# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-01 21:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name='Created')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('created_at', models.DateTimeField(verbose_name='Created')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('Player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score_player', to='dashboard.Player')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='Score1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_score1', to='dashboard.Score'),
        ),
        migrations.AddField(
            model_name='game',
            name='Score2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_Score2', to='dashboard.Score'),
        ),
        migrations.AddField(
            model_name='game',
            name='Winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_winner', to='dashboard.Player'),
        ),
    ]
