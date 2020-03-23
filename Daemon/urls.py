from django.urls import path
from . import views

urlpatterns = [
    path("daemon/powers/<int:power_id>", views.view_power),
    path("daemon/powers", views.all_powers),
    path("daemon/register_power", views.register_power),
    path("", views.choose),
]