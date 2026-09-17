from django.db import models

# Create your models here.




class Project(models.Model):
    name = models.CharField(max_length=200) # Le estámos indicando que vamos a crear una columna "name" y que dentro va a contener una caja de texto que como máximo va a tener 200 caracteres

class Task(models.Model):
    title = models.CharField(max_length=100) # Models.CharField es para textos pequeños
    desciption = models.TextField() # Models.TextField es para textos más grandes
    project =  models.ForeignKey(Project, on_delete=models.CASCADE) # ForeignKey es la clave foranea de las bases de datos, con solo colocar entre los parentesis el nombre de la tabla o clase ya se relaciona. Añadimos on_delete=models.CASCAdE para indicar que si eliminamos el proyecto se eliminarán todos los registros








