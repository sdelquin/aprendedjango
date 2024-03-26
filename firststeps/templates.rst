##########
Plantillas
##########

Las plantillas nos permiten diseñar el aspecto visual de nuestro proyecto. Podemos incorporar información dinámica, lo que las hace muy versátiles.

Una plantilla en Django está habitualmente escrita en lenguaje "html" e incorpora fragmentos de código específicos del `lenguaje de plantillas de Django`_.

**************************
Dónde viven las plantillas
**************************

Una plantilla es un archivo, habitualmente con extensión ``.html`` y que reside en alguna carpeta de nuestro proyecto.

Las plantillas vinculadas con una aplicación ``app`` deberían [#template-loaders]_ residir en la subcarpeta ``templates/app/`` de dicha aplicación. Ejemplo:

+-----------+----------------------------+
|    App    |     Ruta de plantillas     |
+===========+============================+
| ``songs`` | ``songs/templates/songs/`` |
+-----------+----------------------------+

Esto, a priori, puede parecer repetitivo. Pero la razón de hacerlo así se debe a que Django busca las plantillas en todas las carpetas ``templates`` de las aplicaciones dadas de alta en el proyecto.

Por lo tanto, siguiendo este esquema podemos crear un cierto "namespace" o espacio de nombres para las plantillas de cada aplicación.

.. figure:: images/templates/load-template.svg
    :align: center

    Carga de plantillas en Django

******************
Creando plantillas
******************

A continuación vamos a empezar a crear plantillas para poder mostrar información de nuestra aplicación.

Plantilla de lista
==================

Supongamos una primera plantilla que se encarga de mostrar todas las canciones almacenadas en la base de datos de ``musicalia``.

.. code-block:: htmldjango
    :caption: :fa:`r:file-lines#green` ``songs/templates/songs/song/list.html``
    :linenos:

    <ul>
      {% for song in songs %}
        <li>{{ song }}</li>
      {% endfor %}
    </ul>
    
Analicemos cada línea por separado:

- **L1** → Usaremos una etiqueta *html* ``<ul>`` para construir una lista.
- **L2** → Usamos un **bucle** para recorrer las canciones. Esta construcción en Django recibe el nombre de **template tag** (etiqueta de plantilla).
- **L3** → Usamos una etiqueta ``<li>`` y añadimos la canción en concreto que nos viene del bucle.
- **L4** → Cerramos la etiqueta de plantilla del bucle.
- **L5** → Cerramos la etiqueta *html* de lista.

Conceptos que se deben manejar:

Contexto:
  Es el conjunto de variables al que una plantilla tiene acceso. En el ejemplo anterior la variable ``songs`` está en el contexto ya que se ha pasado de forma explícita desde la vista.

Etiqueta de plantilla:
  Las etiquetas de plantilla se escriben usando los delimitadores ``{% %}``. Existe una amplia variedad de `etiquetas de plantilla predefinidas`_ en Django.

Acceso a variable:
  Para acceder a una variable en una plantilla usamos los delimitadores ``{{ }}``.

Si ahora accedemos a http://localhost:8000/song/ veremos la lista de canciones disponibles:

.. figure:: images/templates/song-list.png
    :align: center

    Plantilla de lista de canciones

Plantilla de detalle
====================

Es muy habitual implementar una plantilla para ver los detalles de un objeto en concreto. En nuestro ejemplo vamos a implementar una plantilla para mostrar la información de una canción (objeto de tipo ``Song``).

.. code-block:: htmldjango
    :caption: :fa:`r:file-lines#green` ``songs/templates/songs/song/detail.html``
    :linenos:

    <table>
      <tr>
        <th>Nombre</th>
        <td>{{ song.name }}</td>
      </tr>
      <tr>
        <th>Cantante</th>
        <td>{{ song.singer }}</td>
      </tr>
      <tr>
        <th>Duración</th>
        <td>{{ song.length }} minutos</td>
      </tr>
    </table>

Se puede ver que en las líneas L4, L8 y L12 estamos accediendo a los atributos de modelo del objeto ``song`` que se ha pasado al contexto de la plantilla desde la vista correspondiente.

Si ahora accedemos a http://localhost:8000/song/1/ veremos el detalle de la canción con ``pk=1``:

.. figure:: images/templates/song-detail.png
    :align: center

    Plantilla de detalle de canción




.. _lenguaje de plantillas de Django: https://docs.djangoproject.com/en/dev/ref/templates/language/
.. _etiquetas de plantilla predefinidas: https://docs.djangoproject.com/en/dev/ref/templates/builtins/#built-in-tag-reference



.. [#template-loaders] Se considera una buena práctica que las plantillas vinculadas con una aplicación residan en dicha aplicación, pero hay `otras formas <https://docs.djangoproject.com/en/dev/topics/templates/#loaders>`_ de configurar los cargadores de plantillas en Django.

