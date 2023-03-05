from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.decorators.http import require_http_methods
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.decorators import login_required, permission_required
import datetime
import time
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, PsForm, UserForm, PersonForm, EPersonForm
from .models import Person, Playstation, Nintendo, Xbox, Pc, OldSchool
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from itertools import chain


def serve_all_games(req):
    msg = 'NO Games Have Been Found'
    findp = Playstation.objects.all()
    findx = Xbox.objects.all()
    findn = Nintendo.objects.all()
    findpc = Pc.objects.all()
    findo = OldSchool.objects.all()
    find = list(chain(findx, findp, findn, findo, findpc))
    return render(request=req, template_name="my_app/full-game-list.html", context={'games': find,
                                                                                    'msg': msg})


def home(req):
    if req.user.is_authenticated:
        user = User.objects.get(username=req.user.username)
        return render(request=req, template_name="my_app/home.html", context={'name': user})
    else:
        return render(request=req, template_name="my_app/home.html")


def serve_ps_games(req):
    msg = 'NO Games Have Been Found'
    find = Playstation.objects.all()
    return render(request=req, template_name="my_app/ps-Games-list.html", context={'games': find,
                                                                                   'msg': msg})


def serve_nit_games(req):
    msg = 'NO Games Have Been Found'
    find = Nintendo.objects.all()
    return render(request=req, template_name="my_app/nit-Game-list.html", context={'games': find,
                                                                                   'msg': msg})


def show_game_info(req, gid):
    game = Playstation.objects.get(pk=gid)
    if req.method == "GET":
        form = PsForm(instance=game)
        return render(request=req, template_name="my_app/show_game_info.html",
                      context={'form': form, 'gid': gid})

    elif req.method == 'POST':
        form = PsForm(req.POST, req.FILES, instance=game)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return redirect('login')


def logout_user(req):
    if req.user.is_authenticated:
        logout(request=req)
    return redirect('login')


# @user_passes_test(lambda u: u.is_superuser)
@permission_required('my_app.delete_person')
def user_list(req):
    if user_passes_test:
        msg = 'NO User Have Been Found'
        find = Person.objects.all()
        return render(request=req, template_name="my_app/user-list.html", context={'person': find,
                                                                                   'msg': msg})
    else:
        redirect('my_app/home')


def login_user(req):
    if req.method == "GET":
        return render(request=req, template_name="my_app/login.html",
                      context={"form": LoginForm(),
                               'action': 'login'})

    elif req.method == "POST":
        un = req.POST.get("username")
        pw = req.POST.get("password")
        user = authenticate(req, username=un, password=pw)
        if user is None:
            return redirect("login")
        else:
            login(request=req, user=user)
            return redirect('home')


def del_user(req, pid):
    person = Person.objects.get(pk=pid)
    messages.success(req, f'Item Id ->{person.id}<-Deleted successfully !')
    person.delete()
    return redirect('ulist')


@login_required
def add_game(req):
    if req.method == 'GET':
        return render(request=req, template_name="my_app/gameupload.html",
                      context={"form": PsForm()})
    elif req.method == 'POST':
        form = PsForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return render(request=req, template_name="my_app/home.html")
        else:
            messages.error(req, f' error uploading -> Game <- !')
            return render(request=req, template_name="my_app/gameupload.html",
                          context={"form": PsForm()})


def create_user(req):
    if req.method == "GET":
        return render(request=req, template_name="my_app/signup.html",
                      context={'userform': UserForm(),
                               "person_form": PersonForm()})

    elif req.method == 'POST':
        userform = UserForm(data=req.POST)
        person_form = PersonForm(data=req.POST)
        if userform.is_valid() and person_form.is_valid():
            user = userform.save()
            person_form.instance.user = user
            person_form.save()
            login(request=req, user=user)
            return redirect("home")
        else:
            return render(request=req, template_name="my_app/signup.html",
                          context={'form': userform})


def show_user_info(req, pid):
    person = Person.objects.get(pk=pid)
    user = User.objects.get(username=req.user.username)
    if req.method == "GET":
        form = EPersonForm(instance=person)
        return render(request=req, template_name="my_app/show_user_info.html",
                      context={'form': form, 'pid': pid,
                               'name': user})

    elif req.method == 'POST':
        form = EPersonForm(req.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return redirect('login')
