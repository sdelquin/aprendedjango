################
Puesta en marcha
################

De aquí en adelante trabajaremos sobre un mismo proyecto web que irá creciendo y añadiendo nuevas herramientas a medida que vayamos viendo nuevas secciones.

Este proyecto se denomina **Musicalia** :fa:`music` y pretende ser una plataforma (ficticia) de gestión de canciones, donde podrás compartir, valorar, comentar e incluso "comprar" tu música favorita.

En esta sección se explicará cómo poner en marcha un proyecto Django.

.. warning::
    La explicación se basará en sistema operativo **Linux**.

***************
Entorno virtual
***************

Primero vamos a crear una carpeta ``musicalia`` donde estará el código de nuestro proyecto:

.. code-block:: bash

    $ mkdir musicalia && cd musicalia

A continuación creamos un `entorno virtual`_ donde empaquetar todas las dependencias Python de nuestro proyecto:

.. code-block:: bash

    $ python -m venv .venv --prompt musicalia

Para activar el entorno virtual usamos el script ``activate`` del siguiente modo:

.. code-block:: bash

    $ source .venv/bin/activate

.. tip::
    Cuando activamos el entorno virtual nos aparece delante del "prompt" el nombre del entorno virtual **entre paréntesis**.
    
***********
Instalación
***********

Django es un `paquete de Python <https://pypi.org/project/Django/>`_ que podemos instalar normalmente con ``pip``:

.. code-block:: bash

    $ pip install django

.. caution::
    Importante haber activado el :ref:`entorno virtual <floor2/setup:entorno virtual>` previo a instalar cualquier paquete.

*********************
Creación del proyecto
*********************

Un proyecto Django es una estructura de directorios y archivos que ofrecen funcionalidades web.

Para crear el proyecto, o mejor dicho, para crear el "scaffolding" (andamiaje) del proyecto, debemos lanzar el siguiente comando:

.. code-block:: bash

    $ django-admin startproject musicalia .

.. attention::
    Recordar siempre estar en la carpeta de trabajo (``musicalia`` en este caso) y tener el entorno virtual activado.

Si echamos un vistazo ahora al contenido de la carpeta ``musicalia`` nos encontramos con los siguientes archivos y carpetas:

.. code-block:: bash

    .
    ├── manage.py
    └── musicalia
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py

Veamos para qué sirve cada uno de estos componentes:

:fa:`cube` ``manage.py``
    Este archivo sirve como una interfaz en línea de comandos para realizar diversas tareas como ejecutar el servidor de desarrollo, gestionar la base de datos, ejecutar pruebas y realizar tareas personalizadas.

:fa:`cube` ``musicalia/__init__.py``
    Es un archivo sirve como "placeholder" para indicar que la carpeta ``musicalia`` es un módulo, aunque en versiones "modernas" de Python ya no es necesario incluir este tipo de archivos.

:fa:`cube` ``musicalia/asgi.py``
    Este archivo sirve como punto de entrada para el servidor ASGI (Asynchronous Server Gateway Interface) utilizado para manejar comunicaciones asíncronas en aplicaciones web.

:fa:`cube` ``musicalia/settings.py``
    Este archivo sirve para configurar y personalizar el proyecto, incluyendo la base de datos, las aplicaciones instaladas, las rutas de archivos estáticos, las claves secretas, entre otros ajustes.

:fa:`cube` ``musicalia/urls.py``
    Este archivo sirve para mapear las URLs *de primer nivel* del proyecto a las vistas o aplicaciones correspondientes, determinando cómo se manejan las solicitudes entrantes.

:fa:`cube` ``musicalia/wsgi.py``
    Este archivo sirve como punto de entrada para el servidor WSGI (Web Server Gateway Interface) utilizado para manejar comunicaciones síncronas en aplicaciones web.




.. --------------- Hyperlinks ---------------

.. _entorno virtual: https://docs.python.org/es/3/tutorial/venv.html
