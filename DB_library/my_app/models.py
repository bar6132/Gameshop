from django.db import models
from django.conf import settings
from django.db import models
from django import forms
from django.core.validators import RegexValidator
from django.db.models import CharField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Person(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    city = models.CharField(null=False, max_length=50)
    phone = models.PositiveIntegerField(null=False)
    user = models.OneToOneField(null=True, to=User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Person"

    def __str__(self):
        return f"{self.user}\n" \
               f"{self.id}\n" \
               f"{self.phone}" \

class Playstation(models.Model):
    console_number = models.PositiveIntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ]
    )
    game_name = models.CharField(null=False, max_length=50)
    price = models.PositiveIntegerField(null=False)
    game_img = models.ImageField(null=True, blank=True, upload_to="images/")

    class Meta:
        db_table = "Playstation"

    def __str__(self):
        return f"{self.game_name}"


class Nintendo(models.Model):
    game_name = models.CharField(null=False, max_length=50)
    price = models.PositiveIntegerField(null=False)
    game_img = models.ImageField(null=True, blank=True, upload_to="images/")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "Nintendo"

    def __str__(self):
        return f"{self.game_name}"


class Xbox(models.Model):
    console_name = models.CharField(null=False, max_length=50)
    game_name = models.CharField(null=False, max_length=50)
    price = models.PositiveIntegerField(null=False)
    game_img = models.ImageField(null=True, blank=True, upload_to="images/")


class Pc(models.Model):
    game_name = models.CharField(null=False, max_length=50)
    price = models.PositiveIntegerField(null=False)
    game_img = models.ImageField(null=True, blank=True, upload_to="images/")
    pc_minimum_requirements = models.CharField(null=True, blank=True, max_length=100)


class OldSchool(models.Model):
    console_number = models.PositiveIntegerField(null=True, blank=True)
    console_name = models.CharField(null=False, max_length=50)
    game_name = models.CharField(null=False, max_length=50)
    price = models.PositiveIntegerField(null=False)
    game_img = models.ImageField(null=True, blank=True, upload_to="images/")
