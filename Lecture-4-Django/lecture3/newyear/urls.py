from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index")
    #single route; empty route, single function, with name called index.
]