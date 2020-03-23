from django.urls import path
from . import views

urlpatterns = [
    path("daemon/teams/<int:team_id>", views.view_team),
    path("daemon/teams", views.all_teams),
    path("daemon/register_team_f", views.register_team_finalize),
    path("daemon/register_team", views.register_team),
    path("daemon/powers/<int:power_id>", views.view_power),
    path("daemon/powers", views.all_powers),
    path("daemon/register_power", views.register_power),
    path("", views.choose),
]