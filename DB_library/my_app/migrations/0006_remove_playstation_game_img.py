# Generated by Django 4.1.7 on 2023-02-27 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_playstation_game_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playstation',
            name='game_img',
        ),
    ]
