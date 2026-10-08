from django.shortcuts import render

from .models import Project, Task

from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, JsonResponse

# Create your views here.

def hello(request):
    return render(request, "index.html")

def hellos(request, nombre):
    return HttpResponse(f"<h1>Hello {nombre}</h1>")

def contacto(request):
    return render(request, "pages/contacto.html")

def project(resquest):
    projects = list(Project.objects.values())
    return render(resquest, "pages/project.html")


# ! Para usarlo en proximas tareas
# def task(resquest, title):
#     #task = Task.objects.get(title=title)
#     task = get_object_or_404(Task, title=title) # * Mejor forma de usarlo, salvo cuando sea procesos internos
#     return render(resquest, "pages/task.html")


def task(resquest):
    #task = Task.objects.get(title=title)
    # task = get_object_or_404(Task, title=title) # * Mejor forma de usarlo, salvo cuando sea procesos internos
    return render(resquest, "pages/task.html")