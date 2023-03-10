from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path("", views.home, name="home"),
   path("menu", views.game_menu, name="menu"),
   path("psgl", views.serve_ps_games, name='psgl'),
   path("xbgl", views.serve_xbox_games, name='xbgl'),
   path("gl", views.serve_all_games, name='gl'),
   path("nitgl", views.serve_nit_games, name='nitgl'),
   path("logout", views.logout_user, name="logout"),
   path('login', views.login_user, name="login"),
   path("ulist", views.user_list, name='ulist'),
   path("del/user<str:pid>", views.del_user, name='del/user'),
   path("del/ps<str:gid>", views.del_ps_game, name='del/ps'),
   path('gup', views.add_game, name="gup"),
   path('adx', views.add_xbox_game, name="adx"),
   path('anit', views.add_nit_game, name="anit"),
   path('signup', views.create_user, name='signup'),
   path("ginfo/<str:gid>", views.show_ps_game_info, name="ginfo"),
   path("xbinfo/<str:gid>", views.show_xbox_game_info, name="xbinfo"),
   path("ninfo/<str:gid>", views.show_nit_game_info, name="ninfo"),
   path("uinfo/<str:pid>", views.show_user_info, name="uinfo"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
