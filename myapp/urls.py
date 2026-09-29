# Se ha creado una nueva página donde se guardarán las url relacionadas a esta aplicación

from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.hello),
    path(f'about/', views.about),
    path(f'hellos/<str:nombre>', views.hellos),
]















