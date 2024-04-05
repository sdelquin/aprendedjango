####
URLs
####

Una **url** es una dirección web. Obviamente Django debe "reaccionar" cuando se accede a una determinada url de nuestro proyecto. La forma de "reaccionar" es desencadenar una serie de acciones que suelen estar empaquetadas en una vista.

Es decir, podríamos entender una url como el **nexo** de unión entre las **indicaciones** de un usuario final y las **acciones** implementadas en nuestro código.

Un fichero de *URLs* no es más que un fichero Python que incluye un listado de rutas asociadas con la vista correspondiente que se debe ejecutar.

********************
URLs de primer nivel
********************

Ya hemos visto que, cuando :ref:`se crea un proyecto Django <chapter1/setup:creación del proyecto>`, también se crean varios ficheros entre los que se encuentra un fichero ``urls.py``.

Veamos su contenido:

.. code-block::
    :caption: :fa:`r:file-lines#green` ``musicalia/urls.py``
    :linenos:

    from django.contrib import admin
    from django.urls import path
    
    urlpatterns = [
        path('admin/', admin.site.urls),
    ]
    
Este fichero representa las **urls de primer nivel** ya que son las primeras en analizar cuando llega una petición.

Analicemos cada línea por separado:

- **L1** → Importamos el módulo Django para la `gestión de la interfaz administrativa`_.
- **L2** → Importamos la función Django para `registrar urls`_.
- **L4** → Django espera encontrar en este fichero una variable con el nombre `urlpatterns`_. Esta variable es una lista con las rutas.
- **L5** → Se usa la función `path()`_ para vincular la ruta con su url. En este caso concreto lo que se está haciendo es delegar las *urls* que "cuelgan" de ``admin/`` al fichero ``urls.py`` dentro del módulo administrativo de Django ``admin.site``.

Gracias a este fichero (que viene por defecto) podemos acceder a la :ref:`interfaz administrativa <chapter1/setup:interfaz administrativa>` de Django en la url ``/admin``.

************
Creando URLs
************

Vamos a empezar por el caso de uso en el que queremos listar todas las canciones que hay en el proyecto ``musicalia``. 

Dado que estamos trabajando con la aplicación ``tracks`` podríamos definir la url del listado de canciones en ``/tracks/``

Incluyendo URLs
===============

Para empezar debemos indicar en las urls de primer nivel que todo aquello que empiece por ``/tracks`` sea gestionado por la propia aplicación ``tracks``:

.. code-block::
    :caption: :fa:`r:file-lines#green` ``musicalia/urls.py``
    :linenos:
    :emphasize-lines: 6

    from django.contrib import admin
    from django.urls import include, path
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('tracks/', include('tracks.urls')),
    ]
    
Hemos añadido la **L6** que incluye las urls de la aplicación ``tracks`` para aquellas rutas que estén bajo ``/tracks``. Nótese que se ha usado la cadena de texto ``'tracks.urls'`` en vez de importar directamente el módulo. Esto nos puede facilitar la creación de urls.

URLs de aplicación
==================

Ahora ya estamos en disposición de crear las urls propias de la aplicación ``tracks``.

URL de listado
--------------

Empezaremos por crear una url en la aplicación ``tracks`` de cara a mostrar un listado de todas las canciones.

Para ello debemos crear el fichero ``tracks/urls.py``:

.. code-block::
    :caption: :fa:`r:file-lines#green` ``tracks/urls.py``
    :linenos:

    from django.urls import path
    
    from . import views
    
    app_name = 'tracks'

    urlpatterns = [
        path('', views.track_list, name='track_list'),
    ]
    
Analicemos cada línea por separado:

- **L3** → Importamos las **vistas** de la aplicación actual (``tracks``).
- **L5** → Definimos el **espacio de nombres** [#namespace]_ ``tracks`` para las urls de esta aplicación. Django espera ver una variable llamada ``app_name`` con esta interpretación.
- **L6** → **Registramos** la url usando la función ``path()`` y pasando estos tres argumentos:
    - ``''`` Es la url que queremos gestionar. Al ser cadena vacía indicamos que se trata del raíz ``/``. Pero ojo porque venimos de las urls de primer nivel. Por lo tanto en este caso estamos manejando la url ``/tracks/``
    - ``views.track_list`` Es la vista que se lanzará si la url casa con el patrón indicado.
    - ``'track_list'`` Es el nombre que le damos a esta url. Este argumento es muy importante ya que nos permite referenciar esta url sin tener que "hardcodear" la ruta. Dado que ya hemos dado un espacio de nombres, podemos hacer referencia a esta url con ``tracks:track_list``.

.. caution::
    A diferencia de otros ficheros, el archivo ``urls.py`` de cada aplicación **no se crea** cuando creamos una nueva aplicación Django.

URL de detalle
--------------

Si damos un paso más podemos preparar una url en la que mostraremos el detalle de una canción en concreto:

.. code-block::
    :caption: :fa:`r:file-lines#green` ``tracks/urls.py``
    :linenos:
    :emphasize-lines: 9

    from django.urls import path
    
    from . import views
    
    app_name = 'tracks'

    urlpatterns = [
        path('', views.track_list, name='track_list'),
        path('<pk>/', views.track_detail, name='track_detail'),
    ]

En esta nueva línea introducida **L9** nos damos cuenta de la existencia de un "parámetro" en la url identificado por ``<pk>``. En este caso hace referencia a "primary key" (clave primaria) de la canción en cuestión.

Django pasa este parámetro ``pk`` a la vista para que pueda manejar el detalle de la canción correspondiente.

********************
Conversores de rutas
********************

En una url podemos hacer uso de ángulos ``<>`` lo que nos permite introducir partes dinámicas en la url. Estos parámetros pueden venir precedidos por `conversores de rutas`_ mediante dos puntos ``:``

En el caso de la *url de detalle* de cada canción vista anteriormente, podríamos haber incluido un conversor de ruta sobre la "primary key" de la canción [#primarykey]_:

.. code-block::
    :caption: :fa:`r:file-lines#green` ``tracks/urls.py``
    :linenos:
    :lineno-start: 7
    :emphasize-lines: 3

    urlpatterns = [
        ...
        path('<int:pk>/', views.track_detail, name='track_detail'),
    ]

Un **conversor de ruta** es una anotación en la que indicamos el tipo al que se debe convertir un determinado argumento de url cuando invocamos a la vista correspondiente. Adicionalmente permite establecer (y comprobar) el formato de entrada del citado argumento.

.. csv-table:: Conversores de ruta en Django
    :file: tables/path-converters.csv
    :header-rows: 1
    :widths: 20, 50, 20

.. tip::
    Si no especificamos conversor de ruta se aplicará por defecto ``str``.



.. [#namespace] Un espacio de nombres o "namespace" es un contenedor abstracto en el que un grupo de uno o más identificadores únicos pueden existir.
.. [#primarykey] Habitualmente la clave primaria de un objeto (ORM) suele ser un valor entero representando el identificador único vinculado a la tabla de la base de datos.

.. _gestión de la interfaz administrativa: https://docs.djangoproject.com/en/dev/ref/contrib/#admin
.. _registrar urls: https://docs.djangoproject.com/en/dev/ref/urls/#path
.. _path(): https://docs.djangoproject.com/en/dev/ref/urls/#path
.. _urlpatterns: https://docs.djangoproject.com/en/dev/topics/http/urls/#syntax-of-the-urlpatterns-variable
.. _conversores de rutas: https://docs.djangoproject.com/en/dev/topics/http/urls/#path-converters
