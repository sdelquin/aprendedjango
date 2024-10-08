######
Django
######

`Django`_ es un framework de desarrollo web de alto nivel, gratuito y de código abierto, **escrito en Python**.

Se utiliza para crear aplicaciones web de forma rápida y segura, ya que proporciona una estructura lista para usar, incluyendo funcionalidades comunes como autenticación de usuarios, administración de contenido o manejo de formularios, entre otros. Django es altamente escalable y puede manejar miles de solicitudes, y su arquitectura está diseñada para utilizar eficientemente el hardware del sistema. Además, ofrece características avanzadas de seguridad y es ampliamente utilizado en la industria.

Fue creado por `Adrian Holovaty`_ , `Simon Willison`_, `Jacob Kaplan-Moss`_ y `Wilson Miner`_ en 2005.

.. image:: images/django/django-logo.svg
    :align: center

****************
¿Por qué Django?
****************

El nombre "Django" fue elegido en honor al músico de jazz `Django Reinhardt`_. Django Reinhardt fue un guitarrista y compositor belga de origen gitano que es considerado uno de los músicos más influyentes en la historia del jazz europeo. Fue famoso por su estilo único de tocar la guitarra y por su contribución al desarrollo del jazz en la década de 1930 y 1940.

Los desarrolladores originales de Django, Adrian Holovaty y Simon Willison, eran fanáticos de la música de Django Reinhardt y decidieron nombrar el framework en su honor. El nombre refleja la pasión de los desarrolladores por la música y, al mismo tiempo, transmite la idea de creatividad, innovación y excelencia, valores que también se reflejan en el framework Django.

.. figure:: images/django/django-reinhardt.jpg
    :align: center

    Django Reinhardt (Foto por `Michael Ochs`_ en GettyImages)

*********
Versiones
*********

A continuación se muestran las versiones **mayores** de Django con su año de lanzamiento:

.. csv-table:: Versiones mayores de Django
    :file: tables/django-releases.csv
    :header-rows: 1

***************
Características
***************

A continuación se muestran algunas de las características más importantes de Django:

Diseño basado en el principio de "baterías incluidas":
    Django viene con una variedad de características integradas para ayudar en el desarrollo web, como un ORM (Mapeador Objeto-Relacional) potente para interactuar con la base de datos, un sistema de administración de contenido, autenticación de usuarios, formularios web, entre otros.

Patrón de diseño Modelo-Vista-Controlador (MVC):
    Django sigue un patrón de diseño MVC, aunque lo llama "Model-Template-View" -- MTV (*modelo-vista-plantilla*). Este patrón proporciona una estructura organizativa para el código, lo que facilita el mantenimiento y la escalabilidad de las aplicaciones.

ORM (Mapeador Objeto-Relacional):
    Django incluye su propio ORM («Object Relational Mapping») que permite interactuar con la base de datos utilizando objetos Python en lugar de consultas SQL directas. Esto simplifica el acceso y la manipulación de datos, al tiempo que ayuda a prevenir vulnerabilidades como la inyección SQL.

Sistema de plantillas robusto:
    Django proporciona un sistema de plantillas para generar HTML dinámico de manera eficiente y segura. Este sistema permite la separación limpia de la lógica de presentación y el código de la aplicación.

Administrador de Django:
    Django incluye un potente sistema de administración que se genera automáticamente y ofrece una interfaz de administración basada en la configuración del modelo de datos. Facilita la gestión y el mantenimiento de los datos de la aplicación sin necesidad de escribir código adicional.

Seguridad integrada:
    Django se preocupa por la seguridad y viene con características integradas para proteger las aplicaciones web contra vulnerabilidades comunes, como la protección contra ataques de inyección de código SQL o ataques de Cross-Site Scripting (XSS), entre otros.

Escalabilidad y rendimiento:
    Django está diseñado para ser escalable y manejar aplicaciones de cualquier tamaño. Ofrece herramientas para caché de datos, fragmentación de caché, almacenamiento en caché de consultas de base de datos y otras técnicas para mejorar el rendimiento de las aplicaciones.

Soporte para internacionalización y localización:
    Django facilita la creación de aplicaciones web multilingües gracias a su soporte integrado para la internacionalización y la localización. Esto permite que las aplicaciones se adapten a diferentes idiomas y regiones de forma sencilla.

Estas y otras funcionalidades hacen que Django sea **uno de los frameworks web más populares y potentes disponibles en el ecosistema de desarrollo web de Python**.

******************
¿Quién usa Django?
******************

Grandes empresas y sitios destacados que utilizan Django incluyen:

.. image:: images/django/who-uses-django.svg
    :align: center

Estas empresas confían en Django debido a su alta calidad, seguridad y funcionalidades, respaldadas por una sólida infraestructura de soporte y una comunidad activa.

Comparando con otras tecnologías
================================

En la encuesta a desarrolladores/as de `Stack Overflow (2024)`_, Django ocupaba el décimo puesto de los frameworks web más utilizados:

.. image:: images/django/stackoverflow-survey-2024.png
    :align: center



.. --------------- Hyperlinks ---------------

.. _Django: https://www.djangoproject.com/
.. _Django Reinhardt: https://es.wikipedia.org/wiki/Django_Reinhardt
.. _Adrian Holovaty: https://es.wikipedia.org/wiki/Adrian_Holovaty
.. _Simon Willison: https://es.wikipedia.org/wiki/Simon_Willison
.. _Jacob Kaplan-Moss: https://jacobian.org/
.. _Wilson Miner: https://wilsonminer.com/
.. _Michael Ochs: https://www.gettyimages.es/search/photographer?photographer=Michael%20Ochs%20Archives
.. _Stack Overflow (2024): https://survey.stackoverflow.co/2024/technology/#1-web-frameworks-and-technologies
