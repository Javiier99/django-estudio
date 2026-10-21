from django.shortcuts import render

from .models import Project, Task

from django.shortcuts import get_object_or_404, render, redirect

from django.http import HttpResponse, JsonResponse

from .forms import CreateNewTask, CreateNewProject

# Create your views here.

def hello(request):
    title = "Locura NENE"
    return render(request, "index.html", {
        'title' : title
    })

def hellos(request, nombre):
    return HttpResponse(f"<h1>Hello {nombre}</h1>")

def contacto(request):
    user_name = {
        "nombre" : "Javier"
    }
    return render(request, "pages/contacto.html", {
        'user_name' : user_name 
    })

def project(resquest):
    projects = list(Project.objects.values())
    return render(resquest, "pages/project.html", {
        'projects' : projects
    })


# ! Para usarlo en proximas tareas
# def task(resquest, title):
#     #task = Task.objects.get(title=title)
#     task = get_object_or_404(Task, title=title) # * Mejor forma de usarlo, salvo cuando sea procesos internos
#     return render(resquest, "pages/task.html")


def task(resquest):
    #task = Task.objects.get(title=title)
    # task = get_object_or_404(Task, title=title) # * Mejor forma de usarlo, salvo cuando sea procesos internos
    tasks = Task.objects.all()
    return render(resquest, "pages/task.html", {
        'tasks' : tasks
    })


def formulario(resquest):
    if resquest.method == "GET":
        return render(resquest, "pages/formulario.html", {
            'form' : CreateNewTask()
        })
    else:
        Task.objects.create(title=resquest.POST['title'], desciption=resquest.POST['description'], project_id=3) # * Añadimos esta nueva línea para ir guardando los datos
        return redirect('/task/') # * Retornamos y redirigimos la página a otro sitio




def create_projects(resquest):
    return render(resquest, "projectt/create_project.html", {
        'form_project' : CreateNewProject()
    })