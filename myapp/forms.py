

from django  import forms


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de la tarea", max_length=200) # Con esto creamos el título con su input y su label además le estámos diciento que la longitud máxima que va acontener este input es de 200
    description = forms.CharField(widget=forms.Textarea) # Con esto creamos la descripción su input y label además indicamos que no queremos que sea un requisito contestarlo

