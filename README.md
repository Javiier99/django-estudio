# 📚 Mi Diario de Aprendizaje en Django

## 🎯 Conceptos Clave Aprendidos

### 1. Vistas y Gestión de Peticiones (`views.py`)
- **Diferencia entre GET y POST:** Comprendí que la primera vez que un usuario entra a una página se realiza una petición `GET`, mientras que al enviar un formulario se utiliza `POST`.
- **Estructuración de Vistas:** Aprendí a separar la lógica para devolver el formulario vacío en `GET` y procesar/guardar los datos en la base de datos en `POST`.
- **Manejo seguro con `get_object_or_404`:** Aprendí a sustituir `.get()` por `get_object_or_404()` de `django.shortcuts` para evitar errores que rompan el servidor cuando se busca un registro por ID que no existe, devolviendo una página 404 limpia.
- **Redirecciones:** Uso de `redirect()` para redirigir al usuario tras procesar y guardar un formulario, evitando envíos duplicados al refrescar la página.

---

### 2. Formulación y Formularios (`forms.py`)
- **Creación de clases de formulario:** Uso de `forms.Form` en `forms.py` para definir campos como `CharField` (con `max_length` y `label`) y personalizar widgets como `forms.Textarea`.
- **Acceso a datos:** Diferencia entre extraer datos directamente de `request.POST` y usar `cleaned_data` tras validar los datos.

---

### 3. Plantillas HTML y Sintaxis de Django
- **Diferencia de sintaxis:**
  - `{{ variable }}` (Doble llave) para **imprimir valores** en el HTML (como `{{ form.as_p }}` o `{{ project.name }}`).
  - `{% etiqueta %}` para **lógica y comandos** (`{% extends %}`, `{% block %}`, `{% load static %}`, `{% csrf_token %}`).
- **Iteración de listas y objetos:** Cómo recorrer un *QuerySet* enviado desde la vista (`Project.objects.all()`) y acceder a sus campos en el HTML (`{{ project.id }}`, `{{ project.name }}`).
- **Uso correcto de `{% url %}`:** Aprendí que al pasar variables de un bucle a una ruta dinámica no se deben usar comillas en la variable:
  - `{% url 'project_detail' project.id %}` (correcto).

---

### 4. Configuración de Archivos Estáticos (Imágenes)
- **Carpeta `static` en la raíz:** Aprendí a organizar los recursos estáticos (imágenes, CSS, JS) en una carpeta `static/` ubicada en la raíz del proyecto (al mismo nivel que `manage.py`).
- **Configuración en `settings.py`:** Uso de `STATIC_URL` y configuración de `STATICFILES_DIRS = [ BASE_DIR / 'static' ]` para que Django reconozca la carpeta global.
- **Renderizado en HTML:** Carga del tag `{% load static %}` al inicio de la plantilla y uso de `{% static 'landscape.jpg' %}` en el atributo `src` de las imágenes.

---

## 🛠️ Errores Resueltos durante el Aprendizaje

Durante las prácticas me encontré con varios errores comunes de Django y aprendí a corregirlos:

1. **`MultiValueDictKeyError`:** 
   - *Causa:* Ocurre al intentar leer un campo de `request.GET` cuando la petición vino por `POST`, o si falta el atributo `name="..."` en el `<input>` del HTML.
   - *Solución:* Asegurar el uso de `request.POST` y verificar los atributos `name` del formulario.

2. **`TemplateSyntaxError: Invalid block tag`:**
   - *Causa:* Intentar renderizar una variable de formulario o bloque usando la sintaxis de etiqueta `{% form %}` en lugar de la sintaxis de variable.
   - *Solución:* Cambiar la sintaxis a doble llave `{{ form }}`.

3. **`DoesNotExist` al buscar por ID:**
   - *Causa:* Intentar acceder a una URL con un ID que no existe en la base de datos mediante `.get(id=id)`.
   - *Solución:* Usar `get_object_or_404(Modelo, id=id)`.

4. **Imágenes estáticas no cargadas (404):**
   - *Causa:* Ubicación incorrecta de la carpeta `static` (p. ej. dentro de la carpeta de configuración `config/`) o falta de la variable `STATICFILES_DIRS` en `settings.py`.
   - *Solución:* Mover la carpeta `static` a la raíz del proyecto y registrar la ruta en `settings.py`.


   