################
Puesta en marcha
################

En esta sección se explicará cómo poner en marcha un proyecto Django.

.. warning::
    La explicación se basará en sistema operativo **Linux**.

***************
Entorno virtual
***************

Primero vamos a crear una carpeta ``hola`` donde estará el código de nuestro proyecto:

.. code-block:: bash

    $ mkdir hola
    $ cd hola

A continuación creamos un `entorno virtual`_ donde empaquetar todas las dependencias Python de nuestro proyecto:

.. code-block:: bash

    $ python -m venv .venv --prompt hola

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



.. --------------- Hyperlinks ---------------

.. _entorno virtual: https://docs.python.org/es/3/tutorial/venv.html
