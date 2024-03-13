from django.urls import path
from . import views

app_name = "stockmanager"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="addStock"),
]
