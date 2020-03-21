from django.urls import path
from . import views

urlpatterns = [
    path("registry/<int:id>/edit", views.registry_edit),
    path("registry/add", views.registry_add),
    path("registry/<int:id>", views.registry_viewone),
    path("registry", views.registry_viewall),
    path("welcome/<int:user_id>", views.welcome),
    path("register", views.register),
    path("login", views.login),
    path("", views.choose),
]