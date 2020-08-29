from django.urls import path

from . import views #dot (.) is from a current directory.

urlpatterns = [
    path("", views.index, name="index"),    #if left blank on browser, it will use index bec path("",) is blank.
    path("richard", views.richard, name="richard"), #this will use /hello/richard
    path("ruby", views.ruby, name="ruby"),
]   
