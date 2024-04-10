#######
Modelos
#######

Ya hemos visto los :ref:`tipos de campos "básicos" <chapter1/models:tipos de campos>` para un modelo de Django. Ahora profundizaremos un poco más sobre esto descubriendo nuevas posibilidades.

*************
Claves ajenas
*************

Una de las características más potentes que tienen las bases de datos relacionales es su capacidad para crear precisamente relaciones entre entidades (modelos/tablas). Estas relaciones suelen llevarse a cabo a través de las llamadas "Foreign Key" o **claves ajenas**.

Una clave ajena en una base de datos es un atributo que establece una relación entre dos tablas relacionales. Se utiliza para vincular registros de una tabla con registros correspondientes en otra tabla, referenciando la clave principal de esta última. Esto garantiza la integridad referencial y permite acciones como la actualización o eliminación de registros relacionados de manera consistente, manteniendo la coherencia de los datos en la base de datos.

Nuevo modelo
============

Para poder generar una relación necesitamos, al menos, dos modelos. Hasta el momento hemos estado trabajando con un único modelo ``tracks.Track`` que disponía de tres campos: ``name``, ``singer`` y ``length``.

Parece que tiene sentido normalizar [#normalizar]_ la base de datos y crear un modelo ``Artist`` que almacene la información propia del cantante/grupo/banda (concepto "artista" en general).

Para ello vamos a :ref:`crear una nueva aplicación <chapter1/apps:creando aplicaciones>` llamada ``artists``:

.. code-block:: console

    $ python manage.py startapp artists

Para "activar" la aplicación no podemos olvidar añadirla a ``settings.py``:

.. code-block::
    :emphasize-lines: 9

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'tracks.apps.TracksConfig',
        'artists.apps.ArtistsConfig',
    ]

Y ahora nos toca crear el modelo ``Artist``. Este modelo, como hemos dicho, se encargará de almacenar los cantantes (o grupos) que tengamos en nuestro proyecto:

.. code-block::
    :caption: :fa:`r:file-lines#green` ``artists/models.py``
    :linenos:

    from django.db import models
    
    
    class Artist(models.Model):
        name = models.CharField(max_length=256)
        starting_year = models.PositiveSmallIntegerField()
        website = models.URLField()

        def __str__(self):
            return self.name
    
Ahora creamos las migraciones correspondientes:

.. code-block:: console

    $ python manage.py makemigrations artists
    Migrations for 'artists':
      artists/migrations/0001_initial.py
        - Create model Artist


Y por último, las aplicamos:

.. code-block:: console

    $ python manage.py migrate
    Operations to perform:
      Apply all migrations: admin, artists, auth, contenttypes, sessions, tracks
    Running migrations:
      Applying artists.0001_initial... OK

Vamos a añadir un par de :strike:`artistas` bandas míticas a nuestro proyecto. Para ello abrimos una consola interactiva de Django y escribimos lo siguiente::

    >>> from artists.models import Artist
    
    >>> Artist.objects.create(name='Oasis', starting_year=1991, website='https://oasisinet.com/')
    <Artist: Oasis>
    >>> Artist.objects.create(name='Queen', starting_year=1970, website='https://www.queenonline.com/')
    <Artist: Queen>

Vinculando modelos
==================

El objetivo ahora es vincular el modelo ``Track`` con el modelo ``Artist``. En un diagrama entidad-relación tendríamos lo siguiente:

.. figure:: images/models/erd-foreignkey.svg
    :align: center

    Entidad-Relación

Este diagrama nos dice lo siguiente:

1. Un artista interpreta una o muchas canciones.
2. Una canción es interpretada por uno y solo un artista. [#n-n]_

Por tanto se "transfiere" una clave ajena ("Foreign Key") que estará presente en el modelo ``Track`` y que hará referencia al modelo ``Artist``.

Creando claves ajenas
=====================

Ya estamos en disposición de añadir la clave ajena al modelo ``tracks.Track`` modificando el antiguo campo ``singer`` de tipo ``CharField`` y convirtiéndolo en un campo ``artist`` de tipo `ForeignKey`_:

.. code-block::
    :caption: :fa:`r:file-lines#green` ``tracks/models.py``
    :linenos:
    :emphasize-lines: 6-10

    from django.db import models
    
    
    class Track(models.Model):
        name = models.CharField(max_length=256)
        artist = models.ForeignKey(
            'artists.Artist',
            on_delete=models.CASCADE,
            related_name='tracks',
        )
        length = models.IntegerField()  # in seconds
    
        def __str__(self):
            return self.name

Analicemos las líneas más importantes:

- **L6** → Ahora el campo ``artist`` se convierte en una clave ajena usando el campo ``models.ForeignKey``.
- **L7** → El primer parámetro siempre será el modelo al que hace referencia la clave ajena. Es muy habitual usar una cadena de texto con notación ``'<app>.<Model>'``.
- **L8** → El segundo parámetro requerido es ``on_delete`` en el que debemos especificar el comportamiento a seguir cuando se borra un objeto de referencia. En este caso hemos indicado borrado en cascada.
- **L9** → El parámetro `related_name`_ es muy interesante ya que nos permite dar un nombre a la relación "inversa" entre el objeto de referencia y el objeto relacionado.

A continuación **creamos las migraciones** para estos últimos cambios realizados. Veamos qué ocurre:

.. code-block:: console
    :linenos:

    $ python manage.py makemigrations tracks
    It is impossible to add a non-nullable field 'artist' to track without specifying a default. This is because the database needs something to populate existing rows.
    Please select a fix:
     1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
     2) Quit and manually define a default value in models.py.
    Select an option: 1
    Please enter the default value as valid Python.
    The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
    Type 'exit' to exit this prompt
    >>> 1
    Migrations for 'tracks':
      tracks/migrations/0002_remove_track_singer_track_artist.py
        - Remove field singer from track
        - Add field artist to track

Analicemos las líneas más importantes:

- **L2** → Django nos indica que es imposible añadir el campo **no nulo** ``'artist'`` sin especificar un **valor por defecto**. Esto hace referencia al hecho de que, en el caso de que existieran filas en la tabla, y dado que no admite valores nulos, no sabría que poner en dicho campo.
- **L3** → Django ofrece dos posibilidades:
- **L4** → Proporcionar un valor único por defecto "ahora".
- **L5** → Salir y especificar "manualmente" el valor por defecto en el fichero ``models.py``.
- **L6** → Hemos seleccionado la opción 1)
- **L10** → Se nos abre un intérprete de Python en el que podemos establecer el valor por defecto, incluso usando librerías del sistema. Hemos indicado ``1`` como valor por defecto. Esto implica que si hubieran filas en la tabla ``Track`` todas tendrían como "artista" el que tuviera la clave primaria ``1``.
- **L13** → Se elimina el antiguo campo ``singer``.
- **L14** → Se añade el nuevo campo ``artist``.

Por último debemos aplicar las migraciones para completar el cambio:

.. code-block:: console

    $ python manage.py migrate
    Operations to perform:
      Apply all migrations: admin, artists, auth, contenttypes, sessions, tracks
    Running migrations:
      Applying tracks.0002_remove_track_singer_track_artist... OK

Opciones de borrado
===================

Como hemos visto anteriormente, Django requiere especificar las acciones que se deben tomar al borrar un objeto sobre el que tenemos claves ajenas.

Las opciones disponibles para `on_delete`_ son las siguientes:

:fa:`gear#brown` ``models.CASCADE``:
    Borrado en cascada.

:fa:`gear#brown` ``models.PROTECT``:
    Previene el borrado del objeto siempre que existan referencias elevando una excepción de tipo ``ProtectedError``.

:fa:`gear#brown` ``models.RESTRICT``:
    Previene el borrado del objeto siempre que existan referencias elevando una excepción de tipo ``RestrictedError`` pero con la diferencia de que si hay otra relación de tipo CASCADE sí se borrarán los objetos vinculados.

:fa:`gear#brown` ``models.SET_NULL``:
    Asigna el valor ``NULL`` a la clave ajena. Esto sólo es posible si el campo admite valores nulos.

:fa:`gear#brown` ``models.SET_DEFAULT``:
    Asigna el valor por defecto a la clave ajena. Esto sólo es posible si el campo tiene un valor por defecto.

:fa:`gear#brown` ``models.SET()``:
    Asigna el indicado como parámetro a la clave ajena.

:fa:`gear#brown` ``models.DO_NOTHING``:
    No hace nada. Si la base de datos requiere integridad referencial [#integridad-referencial]_ entonces esto provocará una excepción de tipo ``IntegrityError``.

Manejando el ORM
================

Ahora que ya hemos creado nuestra primera clave ajena, veamos cómo manejar los objetos vinculados a través del ORM de Django.

Asignando claves ajenas
-----------------------

Lo primero que debemos hacer es "arreglar" la asignación de todas las canciones al mismo grupo. Al asignar 1 en la migración como valor para el campo ``artist`` todas las canciones están vinculadas con el artista *Oasis*:

.. code-block::
    :emphasize-lines: 7

    >>> from tracks.models import Track

    >>> for track in Track.objects.all():
    ...     print(f'{track} → {track.artist}')
    ...
    Wonderwall → Oasis
    Bohemian Rhapsody → Oasis

Tendremos que localizar la canción *Bohemiam Rhapsody* y asignarle su artista correcto que es *Queen*:

.. code-block::

    >>> from artists.models import Artist
    >>> from tracks.models import Track

    >>> queen = Artist.objects.get(name='Queen')
    >>> borhap = Track.objects.get(name='Bohemian Rhapsody')

    >>> borhap.artist = queen
    >>> borhap.save()

    >>> borhap.artist
    <Artist: Queen>

Para disponer de más información, vamos a añadir una nueva canción a cada uno de los grupos (artistas)::

    >>> queen = Artist.objects.get(name='Queen')
    >>> oasis = Artist.objects.get(name='Oasis')

    >>> Track.objects.create(name='Live Forever', artist=oasis, length=276)
    <Track: Live Forever>
    >>> Track.objects.create(name='Somebody to love', artist=queen, length=296)
    <Track: Somebody to love>

Consultando relaciones
----------------------

Ahora que ya tenemos todo arreglado y cargadas nuevas canciones, vamos a hacer algunas consultas aprovechando las relaciones de claves ajenas.

Supongamos un primer caso de uso en el que queremos obtener **todas las canciones** del artista *Oasis*. Veamos tres formas de implementar la solución:

Usando la clave ajena directamente:
    .. code-block::

        >>> oasis
        <Artist: Oasis>

        >>> Track.objects.filter(artist=oasis)
        <QuerySet [<Track: Wonderwall>, <Track: Live Forever>]>
    
Usando un atributo de la clave ajena:
    .. code-block::

        >>> Track.objects.filter(artist__name='Oasis')
        <QuerySet [<Track: Wonderwall>, <Track: Live Forever>]>

Usando la relación inversa de la clave ajena:
    .. code-block::

        >>> oasis
        <Artist: Oasis>

        >>> oasis.tracks.all()
        <QuerySet [<Track: Wonderwall>, <Track: Live Forever>]>

El atributo ``tracks`` que aparece ahora en los artistas es el ``related_name`` que se ha definido en la :ref:`clave ajena <chapter2/models:creando claves ajenas>` y permite obtener todos los objetos relacionados (en este caso canciones).

Por supuesto el objecto ``tracks`` permite aplicarle nuevos filtros::

    >>> oasis.tracks.filter(length__lt=260)
    <QuerySet [<Track: Wonderwall>]>

    >>> queen.tracks.filter(length__lt=260)
    <QuerySet []>

*************
Valores nulos
*************

Hay ocasiones en las que necesitamos que un campo de modelo pueda tomar valores nulos, o dicho de otra forma, que su contenido sea **opcional**. En estos casos debemos indicarle a Django dicha circunstancia para que permita que el campo quede sin un valor.

El modelo ``Artist`` dispone de un atributo ``website`` que contiene una URL al sitio web del artista en cuestión. Pero es altamente probable que no todos los artistas dispongan de un sitio web propio. Es por ello que conviene indicar que dicho campo debe ser opcional (contener nulos).

Para ello realizamos la siguiente modificación al modelo:

.. code-block::
    :caption: :fa:`r:file-lines#green` ``artists/models.py``
    :linenos:
    :emphasize-lines: 7

    from django.db import models
    
    
    class Artist(models.Model):
        name = models.CharField(max_length=256)
        starting_year = models.PositiveSmallIntegerField()
        website = models.URLField(blank=True)
    
        def __str__(self):
            return self.name
    
Hemos indicado con ``blank=True`` que el campo ``website`` puede contener valores en blanco.

Como siempre, creamos la migración del cambio:

.. code-block:: console

    $ python manage.py makemigrations artists
    Migrations for 'artists':
      artists/migrations/0002_alter_artist_website.py
        - Alter field website on artist

Y aplicamos dicha migración:

.. code-block:: console

    $ python manage.py migrate
    Operations to perform:
      Apply all migrations: admin, artists, auth, contenttypes, sessions, tracks
    Running migrations:
      Applying artists.0002_alter_artist_website... OK

Sabores de nulo
===============

En el contexto de bases de datos, el término "nulo" se refiere a la ausencia de un valor válido en un campo de una tabla. Esto significa que no hay ningún dato almacenado en ese campo para una determinada fila o registro.

Django ofrece dos parámetros para manejar la "ausencia de valor":

- ``blank=True`` para indicar que el campo puede estar vacío.
- ``null=True`` para indicar que si el campo está vacío se almacene un ``NULL`` en la correspondiente tabla.

Pero la "ausencia de valor" puede almacenarse de varias maneras dependiendo del tipo de campo:

- Para campos de tipo texto la ausencia de valor podría ser la **cadena vacía**.
- Para otro tipo de campos la ausencia de valor podría ser ``NULL``.

Es por ello que para todos los **campos basados en texto** Django **desaconseja utilizar** ``null=True`` ya que esto podría ofrecer dos valores para el mismo concepto de "ausencia de valor": el valor nulo y la cadena vacía.

.. csv-table:: Especificación de valores nulos
    :file: tables/null.csv
    :header-rows: 1
    :widths: 40, 20, 20

*******************
Valores por defecto
*******************

Otro aspecto a tener en cuenta a la hora de añadir un campo al modelo son los valores por defecto. Es decir, aquellos valores que se usarán en ausencia de valores explícitos para el campo en cuestión.

Continuando con nuestro ejemplo del modelo ``Track`` que representa una canción, podríamos querer almacenar el **número de visitas** que ha tenido esta canción en nuestro proyecto. Parece razonable que este número tenga un valor por defecto de 0, ya que inicialmente nadie ha visitado la canción.

Vamos a agregar un campo ``num_visits`` al modelo ``Track``:

.. code-block::
    :caption: :fa:`r:file-lines#green` ``tracks/models.py``
    :linenos:
    :emphasize-lines: 12

    from django.db import models
    
    
    class Track(models.Model):
        name = models.CharField(max_length=256)
        artist = models.ForeignKey(
            'artists.Artist',
            on_delete=models.CASCADE,
            related_name='tracks',
        )
        length = models.IntegerField()  # in seconds
        num_visits = models.PositiveBigIntegerField(default=0)
    
        def __str__(self):
            return self.name
    
Podemos observar en la **L12** que se ha añadido el campo ``num_visits`` con un valor por defecto ``0``. El tipo de campo elegido es un `PositiveBigIntegerField`_ simplemente porque dispone de un rango más amplio de valores.

Ahora creamos la migración y la aplicamos:

.. code-block:: console

    $ python manage.py makemigrations tracks && python manage.py migrate tracks
    Migrations for 'tracks':
      tracks/migrations/0003_track_num_visits.py
        - Add field num_visits to track
    Operations to perform:
      Apply all migrations: tracks
    Running migrations:
      Applying tracks.0003_track_num_visits... OK

.. caution::
    A diferencia de lo ocurrido cuando agregamos el campo ``artist`` como clave ajena, en este caso la migración no ha dado ningún problema, a pesar de que el campo ``num_visits`` no admite valores nulos. Esto se debe a que tiene un valor por defecto, y en el supuesto caso de que ya existieran filas en la tabla, se rellenarían con dicho valor por defecto.

**************
Clave primaria
**************

Django nos permite definir nuestra **propia clave primaria** si es que no queremos usar la que :ref:`se genera por defecto <chapter1/models:clave primaria>`.

Para ello debemos usar el parámetro `primary_key`_ sobre el campo que queramos convertir en clave primaria. **Suponiendo** que el *nombre del artista* fuera único en el universo de la música, podríamos hacerlo clave primaria de la siguiente manera:

.. code-block::
    :caption: :fa:`r:file-lines#green` ``artists/models.py``
    :linenos:
    :emphasize-lines: 5

    from django.db import models
    
    
    class Artist(models.Model):
        name = models.CharField(primary_key=True, max_length=256)
        starting_year = models.PositiveSmallIntegerField()
        website = models.URLField(blank=True)
    
        def __str__(self):
            return self.name
    
Nótese que en la **L5** hemos añadido la especificación de clave primaria. Con esta modificación ``name`` se convertirá en la nueva clave primaria de la tabla.

.. attention::
    Aunque otra clave se convierta en clave primaria, Django **no elimina** automáticamente el campo ``id`` de la tabla. Si es eso lo que se quiere, se tendrá que hacer "manualmente".

Claves candidatas
=================

Una **clave candidata** en una base de datos es un conjunto de uno o más atributos que pueden identificar de forma única una fila en una tabla, pero aún no han sido designados como clave primaria.

Django ofrece la posibilidad de que los valores que toma un campo sean **únicos**. Por tanto, dicho campo se convertirá en una clave candidata.

Para ello usaremos el parámetro `unique`_ en la especificación del campo en cuestión. Siguiendo el mismo ejemplo que en el caso anterior podríamos **suponer** que el nombre del artista debe ser único:

.. code-block::
    :caption: :fa:`r:file-lines#green` ``artists/models.py``
    :linenos:
    :emphasize-lines: 5

    from django.db import models
    
    
    class Artist(models.Model):
        name = models.CharField(unique=True, max_length=256)
        starting_year = models.PositiveSmallIntegerField()
        website = models.URLField(blank=True)
    
        def __str__(self):
            return self.name

Nótese que en la **L5** hemos añadido la especificación de valores únicos. Con esta modificación ``name`` se convertirá en una clave candidata de la tabla pero el campo ``id`` seguirá estando en la tabla como clave primaria.

********************
Conjunto de opciones
********************

Hay ocasiones en las que nos interesa que un determinado campo de **tipo texto** tome únicamente valores sobre un `conjunto definido de opciones`_.

Aunque hoy en día toda la música se considera global, imaginemos que queremos almacenar en nuestra base de datos el **ámbito de los artistas**. Este ámbito puede ser de 3 tipos:

- Local
- Nacional
- Internacional

Ahora vamos a trasladar este comportamiento a nuestro modelo ``Artist``:

.. code-block::
    :caption: :fa:`r:file-lines#green` ``artists/models.py``
    :emphasize-lines: 5-12, 17-21
    :linenos:

    from django.db import models
    
    
    class Artist(models.Model):
        LOCAL = 'L'
        NATIONAL = 'N'
        INTERNATIONAL = 'I'
        SCOPE_CHOICES = {
            LOCAL: 'Local',
            NATIONAL: 'Nacional',
            INTERNATIONAL: 'Internacional',
        }
    
        name = models.CharField(max_length=256)
        starting_year = models.PositiveSmallIntegerField()
        website = models.URLField(blank=True)
        scope = models.CharField(
            max_length=1,
            choices=SCOPE_CHOICES,
            default=INTERNATIONAL,
        )
    
        def __str__(self):
            return self.name

Analicemos cada línea por separado:

- **L5-L7** → Definimos las posibles opciones como **constantes de clase** asignándoles un *número fijo de caracteres*. [#fixed-chars]_
- **L8-L12** → Introducimos un diccionario (también como constante de clase) en la que se define el "nombre" que va a tener cada opción.
- **L17** → Usaremos siempre un campo de tipo ``CharField`` para este tipo de escenarios.
- **L18** → Indicamos un tamaño máximo de 1 caracter. Esto se debe a que hemos asignado cadenas de texto de tamaño 1 a las opciones (véase L5-L7).
- **L19** → El parámetro ``choices`` es el que nos permite indicar las posibles opciones que puede tomar este campo.
- **L20** → Establecemos el ámbito internacional como valor por defecto para este campo.

Tipos enumerados
================

Django proporciona `tipos enumerados`_ como alternativa para añadir un campo que toma una serie de opciones concretas.

Veamos cómo sería la implementación:

.. code-block::
    :caption: :fa:`r:file-lines#green` ``artists/models.py``
    :linenos:
    :emphasize-lines: 5-8, 13-17

    from django.db import models
    
    
    class Artist(models.Model):
        class Scope(models.TextChoices):
            LOCAL = 'L', 'Local'
            NATIONAL = 'N', 'Nacional'
            INTERNATIONAL = 'I', 'Internacional'
    
        name = models.CharField(max_length=256)
        starting_year = models.PositiveSmallIntegerField()
        website = models.URLField(blank=True)
        scope = models.CharField(
            max_length=1,
            choices=Scope,
            default=Scope.INTERNATIONAL,
        )
    
        def __str__(self):
            return self.name
    
Analicemos cada línea por separado:

- **L5** → Definimos una clase que contendrá las opciones. Esta clase hereda de ``models.TextChoices``.
- **L6-L8** → Se añaden los atributos de clase con las opciones disponibles. Cada atributo viene definido por una tupla donde el primer elemento es el *identificador* y el segundo elemento es la *etiqueta*.
- **L13-L17** → La especificación del campo como ``CharField`` es igual que en el caso anterior pero usando la clase "enumerada" que hemos creado en L5.

Vamos a crear la migración correspondiente y a aplicarla:

.. code-block:: console

    $ python manage.py makemigrations artists
    Migrations for 'artists':
      artists/migrations/0003_artist_scope.py
        - Add field scope to artist
    
    $ python manage.py migrate artists
    Operations to perform:
      Apply all migrations: artists
    Running migrations:
      Applying artists.0003_artist_scope... OK

Acceso a atributos
------------------

Lo primero que vamos a hacer es **obtener el valor del ámbito** para un artista:

.. code-block::
    :linenos:

    >>> from artists.models import Artist

    >>> oasis = Artist.objects.get(name='Oasis')

    >>> oasis.scope
    'I'

    >>> oasis.get_scope_display()
    'Internacional'

Analicemos las líneas más importantes:

- **L5** → Obtenemos el atributo como cualquier otro. En este caso nos devuelve la representación como "cadena de texto".
- **L8** → Django genera un método ``get_<attr>_display()`` con el que podemos obtener la etiqueta asignada al valor.

Ahora vamos a crear un nuevo artista y **asignar un ámbito local**:

.. code-block::
    :linenos:

    >>> pepe = Artist(name='Pepe Benavente', starting_year=1970)

    >>> pepe.scope = Artist.Scope.LOCAL
    >>> pepe.save()

    >>> pepe.get_scope_display()
    'Local'

Analicemos las líneas más importantes:

- **L3** → Asignamos el ámbito a través del atributo de la clase interior que hemos creado.
- **L6** → Comprobamos la etiqueta del valor asignado.

Es posible acceder a las **opciones definidas** en el propio tipo enumerado de la siguiente manera::

    >>> Artist.Scope.choices
    [('L', 'Local'), ('N', 'Nacional'), ('I', 'Internacional')]

También podemos acceder tanto al **nombre** como a la **etiqueta** de una opción concreta::

    >>> Artist.Scope.NATIONAL.name
    'NATIONAL'
    >>> Artist.Scope.NATIONAL.label
    'Nacional'



    
.. _related_name: https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ForeignKey.related_name
.. _ForeignKey: https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ForeignKey
.. _on_delete: https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ForeignKey.on_delete
.. _PositiveBigIntegerField: https://docs.djangoproject.com/en/dev/ref/models/fields/#positivebigintegerfield
.. _primary_key: https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.Field.primary_key
.. _unique: https://docs.djangoproject.com/en/dev/ref/models/fields/#unique
.. _conjunto definido de opciones: https://docs.djangoproject.com/en/dev/ref/models/fields/#choices
.. _tipos enumerados: https://docs.djangoproject.com/en/dev/ref/models/fields/#enumeration-types


.. [#normalizar] "Normalizar" una base de datos se refiere al proceso de organizar la estructura de la base de datos para reducir la redundancia de datos y mejorar la integridad y eficiencia.
.. [#n-n] Sería muy razonable que la relación entre artista y canción fuera de N:N indicando que una canción puede ser cantada por múltiples artistas. En este momento nos quedaremos en un esquema más simple 1:N.
.. [#integridad-referencial] La integridad referencial en una base de datos implica que la clave externa de una tabla de referencia siempre debe aludir a una fila válida de la tabla a la que se haga referencia.
.. [#fixed-chars] No es obligatorio asignar un número fijo de caracteres, pero suele ser útil a la hora de definir el máximo tamaño del campo.
