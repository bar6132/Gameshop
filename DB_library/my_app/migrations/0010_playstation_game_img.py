# Generated by Django 4.1.7 on 2023-02-28 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_remove_playstation_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='playstation',
            name='game_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]