# Generated by Django 4.1.7 on 2023-02-27 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_app', '0007_alter_person_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nintendo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='playstation',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploaded_files'),
        ),
        migrations.AlterField(
            model_name='person',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]