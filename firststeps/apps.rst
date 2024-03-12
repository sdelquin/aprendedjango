############
Aplicaciones
############

Un proyecto Django está formado por aplicaciones. En este contexto podemos entender una aplicación como una "zona" o "sección" de nuestro sitio web.

********************
Creando aplicaciones
********************

Vamos a empezar por lo más obvio de nuestro proyecto que serían **las canciones**. Crearemos una aplicación ``songs``:

.. code-block:: console

    $ python manage.py startapp songs

.. tip::
    Suele ser habitual usar **nombres en plural** para las aplicaciones, pero obviamente depende del contexto y no es una regla fija.

El comando anterior habrá creado una carpeta ``songs`` en la raíz de nuestro proyecto con el siguiente contenido:

.. code-block:: console

    $ tree songs

    songs
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
    
    2 directories, 7 files

Veamos para qué sirve cada uno de estos archivos:

:fa:`cube` ``__init__.py``
    Este tipo de archivos se utilizan para indicar que la carpeta actual es un `paquete`_ en Python.

:fa:`cube` ``admin.py``
    Este archivo permite especificar las características de los modelos de cara a la `interfaz administrativa`_ de Django.

:fa:`cube` ``apps.py``
    Este archivo permite "registrar" la aplicación creada y definir algunas configuraciones a nivel global.

:fa:`cube` ``migrations``
    Esta carpeta contendrá las migraciones (como ficheros) realizadas sobre los modelos de la aplicación actual.

:fa:`cube` ``models.py``
    Este archivo permite escribir los modelos de la aplicación actual.

:fa:`cube` ``tests.py``
    Este archivo permite escribir las pruebas (*tests*) de la aplicación actual.

:fa:`cube` ``views.py``
    Este archivo permite definir las vistas de la aplicación actual.


.. _paquete: https://docs.python.org/3/tutorial/modules.html#packages
.. _interfaz administrativa: https://docs.djangoproject.com/en/dev/ref/contrib/admin/

***********************
Instalando aplicaciones
***********************

Para que Django reconozca una nueva aplicación en nuestro proyecto, necesitamos darla de alta ("instalar") en el fichero ``settings.py``.

Existe una variable ``INSTALLED_APPS`` que contiene una lista con todas las aplicaciones dadas de alta en el proyecto. Si miramos su contenido actual veremos lo siguiente::

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]

Estas aplicaciones están "preinstaladas" cuando creamos el proyecto y son propias del framework Django. Nos proporcionan distintas funcionalidades:

:fa:`cube` `django.contrib.admin`_
    Interfaz administrativa.

:fa:`cube` `django.contrib.auth`_
    Sistema de autenticación.

:fa:`cube` `django.contrib.contenttypes`_
    Herramientas para trabajar con los modelos del proyecto.

:fa:`cube` `django.contrib.sessions`_
    Sistema para almacenar información en sesiones.

:fa:`cube` `django.contrib.staticfiles`_
    Gestión de archivos estáticos.

Por tanto, vamos a añadir nuestra aplicación ``songs`` a la lista ``INSTALLED_APPS`` en el fichero ``settings.py``:

.. code-block::
    :emphasize-lines: 8

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'songs.apps.SongsConfig',
    ]

Cabría preguntarse por qué se añade la línea ``'songs.apps.SongsConfig'``. La clase ``SongsConfig`` que está dentro del módulo ``apps`` en la aplicación ``songs`` es donde reside la configuración global de la aplicación. [#install-app]_

.. tip::
    Es una convención que si una aplicación se llama ``matraca`` entonces la clase de configuración se debería llamar ``MatracaConfig``.

.. ================================================================================================================

.. [#install-app]
    Es posible "instalar" una aplicación únicamente por su nombre, en este caso añadiendo ``'songs'`` a ``INSTALLED_APPS`` pero en ese caso perderíamos la capacidad de `personalizar ciertos aspectos de la aplicación <https://stackoverflow.com/a/60770936>`_ mediante ``SongsConfig``.

.. _django.contrib.admin: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#module-django.contrib.admin
.. _django.contrib.auth: https://docs.djangoproject.com/en/dev/ref/contrib/auth/#django-contrib-auth
.. _django.contrib.contenttypes: https://docs.djangoproject.com/en/dev/ref/contrib/contenttypes/#module-django.contrib.contenttypes
.. _django.contrib.sessions: https://docs.djangoproject.com/en/dev/topics/http/sessions/
.. _django.contrib.staticfiles: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/
