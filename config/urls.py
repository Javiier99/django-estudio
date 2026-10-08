"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from myapp.views import hello # * Lo oculto porque ya no sirve, ya que tenemos la función -> path('', include('myapp.urls'))
# nombre = "javier" # Nombre de una variable
urlpatterns = [
    
    path('admin/', admin.site.urls),
    # path('', hello), # La url raiz que ahora se ha llevado a la aplicación myapp
    # path(f'about/{nombre}', about), # a url about con variable, que se ha llevado  a la aplicación myapp

    path('', include('myapp.urls')) # * Esta función es la que tenemos
]
