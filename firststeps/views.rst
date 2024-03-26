######
Vistas
######

Las vistas en Django constituyen la pieza de software que lleva a cabo la "lógica de negocio" relacionando *urls*, *modelos* y *plantillas*.

Una vista es simplemente una **función** que siempre recibe como primer parámetro la **petición** "http" y como resto de parámetros los indicados en la url correspondiente.

**************
Creando vistas
**************

Cuando creamos una nueva aplicación en nuestro proyecto Django se nos crea un fichero ``views.py`` dentro de dicha aplicación que es donde tenemos que escribir nuestras vistas.

Vista de lista
==============

Vamos a implementar nuestra primera vista que sería aquella que permite listar todas las canciones de nuestro proyecto:

.. code-block::
    :caption: :fa:`r:file-lines#green` ``songs/views.py``
    :linenos:

    from django.http import HttpRequest, HttpResponse
    from django.shortcuts import render
    
    from .models import Song
    
    
    def song_list(request: HttpRequest) -> HttpResponse:
        songs = Song.objects.all()
        return render('songs/song/list.html', dict(songs=songs))
    
Analicemos cada línea por separado:

- **L1** → Estos "imports" **no son necesarios**. Se han incluido en el código a modo de aclaración para que las anotaciones de tipo expliquen por sí mismas los parámetros de la función.
- **L2** → Django proporciona una serie de atajos [#shortcuts]_. En este caso importamos la función `render()`_
- **L4** → Las vistas suelen manejar modelos. En este caso estamos importando el modelo ``Song`` de la propia aplicación ``songs``.
- **L7** → El único parámetro ``request`` es la petición `HttpRequest`_. La función debe devolver una respuesta `HttpResponse`_
- **L8** → Obtenemos todas las canciones.
- **L9** → Utilizamos la función ``render()``. Esta función recibe como primer parámetro la ruta al fichero de **plantilla** y en segundo lugar un diccionario con el **contexto** (variables). Renderiza la plantilla y devuelve la respuesta "http".

Vista de detalle
================

La siguiente vista que vamos a escribir es aquella que se encarga de mostrar el detalle de una determinada canción. En esta vista recibimos un parámetro que viene en la url y que nos indica la clave primaria de la canción en cuestión:

.. code-block::
    :caption: :fa:`r:file-lines#green` ``songs/views.py``
    :linenos:
    :lineno-start: 10

    ...

    def song_detail(request: HttpRequest, pk: int) -> HttpResponse:
        song = Song.objects.get(pk=pk)
        return render(request, 'songs/song/detail.html', dict(song=song))

Analicemos cada línea por separado:

- **L12** → La función no sólo recibe la petición "http" sino la clave primaria de la canción ``pk`` que queremos manejar. Es de tipo entero porque hemos aplicado un :ref:`conversor de ruta <firststeps/urls:conversores de rutas>` en la url.
- **L13** → Obtenemos la canción concreta que nos interesa.
- **L14** → Utilizamos la función ``render()`` pasando en el contexto la canción que hemos obtenido previamente.




.. [#shortcuts] Los `atajos <https://docs.djangoproject.com/en/dev/topics/http/shortcuts/#render>`_ que proporciona Django son los siguientes: ``render()``, ``redirect()``, ``get_object_or_404()`` y ``get_list_or_404()``.

.. _render(): https://docs.djangoproject.com/en/dev/topics/http/shortcuts/#render
.. _HttpRequest: https://docs.djangoproject.com/en/dev/ref/request-response/#httprequest-objects
.. _HttpResponse: https://docs.djangoproject.com/en/dev/ref/request-response/#httpresponse-objects
