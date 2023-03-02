from django.contrib import admin
from .models import Person, Playstation, Nintendo
from django.contrib.sessions.models import Session
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission, Group

admin.site.register(Person)
admin.site.register(Session)
admin.site.register(Playstation)
admin.site.register(ContentType)
admin.site.register(Permission)
admin.site.register(Nintendo)
