- 200917 

- 16 Create new app called tasks 

 - On Terminal:  

 - python manage.py startapp tasks 

 - Go to /lecture/settings.py and add tasks 

  `'tasks',` 

 - /lecture3/urls.py and add tasks. 

`path('tasks/', include("tasks.urls")), ``

 - Create /lecture3/tasks/urls.py 

`from django.urls import path `

`from . import views ``

urlpatterns = [ `

    `path("", views.index, name="index") `

 

 - Go to /lecture3/tasks/views.py 

 - Create /lecture3/tasks/templates/tasks/index.html 

-  Run server 

 - Python manage.py runserver 

- 200921 

- Create a function in /tasks/views.py 
