# Se ha creado una nueva página donde se guardarán las url relacionadas a esta aplicación

from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.hello),
    path(f'contacto/', views.contacto),
    path(f'hellos/<str:nombre>', views.hellos),
    path('project/', views.project),
    # path('task/<str:title>', views.task), #! Para usarlo en proximas tareas
    path('task/', views.task),
    path('form/', views.formulario),
]















