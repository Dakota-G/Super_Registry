from django.urls import path
from . import views

urlpatterns = [
    path("daemon/register_power", views.register_power),
    path("", views.choose),
]