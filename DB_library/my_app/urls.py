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
   # path("edit/user", views.edit_user, name='edit/user'),
   path("del/user<str:pid>", views.del_user, name='del/user'),
   path('gup', views.add_game, name="gup"),
   path('adx', views.add_xbox_game, name="adx"),
   path('anit', views.add_nit_game, name="anit"),
   path('signup', views.create_user, name='signup'),
   path("ginfo/<str:gid>", views.show_game_info, name="ginfo"),
   path("uinfo/<str:pid>", views.show_user_info, name="uinfo"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
