# Generated by Django 3.2.4 on 2022-07-11 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviedb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='release_date',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='title',
        ),
        migrations.RemoveField(
            model_name='role',
            name='lead',
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', through='moviedb.Role', to='moviedb.Actor'),
        ),
        migrations.AlterField(
            model_name='role',
            name='actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='moviedb.actor'),
        ),
        migrations.AlterField(
            model_name='role',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='moviedb.movie'),
        ),
    ]
