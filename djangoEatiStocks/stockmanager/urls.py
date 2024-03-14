from django.urls import path
from . import views

app_name = "stockmanager"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="addStock"),
    path("addTicker/", views.addTickerSearch, name="addTicker"),
    path("tickerList/", views.tickerList, name="tickerList"),
]
