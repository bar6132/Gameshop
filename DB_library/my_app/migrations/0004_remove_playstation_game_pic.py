# Generated by Django 4.1.7 on 2023-02-27 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_playstation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playstation',
            name='game_pic',
        ),
    ]
