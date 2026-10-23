# Se ha creado una nueva página donde se guardarán las url relacionadas a esta aplicación

from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.hello, name="index" ),
    path(f'contacto/', views.contacto, name="contact"),
    path(f'hellos/<str:nombre>', views.hellos, name="hellos"),
    path('project/', views.project, name="project"),
    # path('task/<str:title>', views.task), #! Para usarlo en proximas tareas
    path('taskkkkkk/', views.task, name="task"),
    path('form/', views.formulario),
    path('create_project/', views.create_projects, name="create_project"),
    path('project/<int:id>', views.project_detail, name="project_detail"),
]















