from django.contrib import admin
from .models import Person, Playstation
from django.contrib.sessions.models import Session

admin.site.register(Person)
admin.site.register(Session)
admin.site.register(Playstation)
