import datetime
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime, AdminTimeWidget
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Playstation, User, Person


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)


class PsForm(ModelForm):
    class Meta:
        model = Playstation
        fields = "__all__"


class UserForm(UserCreationForm):
    email = forms.EmailField()


class PersonForm(ModelForm):

    class Meta:
        model = Person
        exclude = ['user']
        fields = '__all__'
