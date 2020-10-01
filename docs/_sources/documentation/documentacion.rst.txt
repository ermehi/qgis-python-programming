Documentación oficial QGIS de referencia
****************************************
La `documentación oficial <http://www.qgis.org/en/docs/index.html>`_ de QGIS está en idioma inglés,
pero algunas partes están traducidas a varios idiomas.

Las principales referencias para el **desarrollador** son la `API QGIS C++ <https://qgis.org/api/3.10/>`_,
la `API PyQGIS – QGIS Python <https://qgis.org/pyqgis/3.10/>`_ y el libro de recetas para el desarrollador PyQGIS
(`PyQGIS cookbook <https://docs.qgis.org/3.10/es/docs/pyqgis_developer_cookbook/>`_).
Estos recursos se complementan con la guía de usuario
(`QGIS User guide <https://docs.qgis.org/3.10/es/docs/user_manual/>`_) y el manual de aprendizaje
(`QGIS Training manual <https://docs.qgis.org/3.10/es/docs/training_manual/>`_).

.. note::   De forma genérica, los **manuales de usuario** (*user guide*) son utilizados para
            describir las características y funcionalidades disponibles en una determinada aplicación informática
            y su forma de uso. Los manuales de usuario explican todas las pantallas y campos.

            Un **manual de aprendizaje** (*training manual*) se redacta de forma diferente y puede estar acompañado
            de ejercicios para que el usuario los complete. Describen una parte específica del sistema, paso a paso,
            pero no explican todas las funcionalidades y características de la herramienta informática.
            Suelen tener más capturas de pantallas que los manuales de usuario.

Webography: PyQGIS online resources
***********************************
En este apartado se aportan un conjunto de recursos de PyQGIS, Python y Qt.

PyQGIS
======

Interactuar con otros usuarios
------------------------------
Una de las ventajas de los proyectos de código abierto es que se puede hablar directamente con otros desarrolladores
y frecuentemente con los desarrolladores principales del proyecto.

Resolución de dudas
^^^^^^^^^^^^^^^^^^^
QGIS tiene tres formas oficiales de apoyar el desarrollo y la resolución de problemas.
En las listas de correo, canales IRC y redes sociales técnicas se puede obtener soporte de otros usuarios:

* `Listas de correo <http://qgis.org/en/site/getinvolved/mailinglists.html>`_:

    * `Developer list <http://lists.osgeo.org/mailman/listinfo/qgis-developer>`_
    * `User list <http://lists.osgeo.org/mailman/listinfo/qgis-user>`_.

* Internet Relay Chat (IRC): para obtener asistencia de usuarios y desarrolladores en tiempo real.
  Esta ayuda es voluntaria y está condicionada a su disponibilidad.
  Se puede acceder al `canal de QGIS <http://webchat.freenode.net/?channels=#qgis>`_ y
  al `registro <http://irclogs.geoapt.com/qgis/>`_ desde el 10/05/2016.
* The Stack Exchange community: Esta red social técnica tiene un subproyecto GIS
  (Geographic Information Systems Stack Exchange) con 36 etiquetas relacionadas con QGIS y PyQGIS en el siguiente
  `enlace <https://gis.stackexchange.com/tags>`_.

Reporte de bugs
^^^^^^^^^^^^^^^
Una manera importante de respaldar el proyecto QGIS, además de financiarlo, es mediante el reporte problemas
(solicitudes de nuevas funcionalidades o errores) aportando un caso de uso detallado y los datos que permiten
a otros replicar el problema, permitiendo acelerar su corrección.
La guía para reportar errores está disponible en el siguiente enlace.
Se recomienda consultar las `indicaciones <https://www.qgis.org/en/site/getinvolved/development/bugreporting.html>`_
antes de reportar un error.

Cada parte del proyecto QGIS tiene un lugar específico donde los problemas se pueden informar, gestionar y discutir.
Dependiendo del área en la que haya encontrado el problema,
la tabla a continuación indica el repositorio correcto para reportarlo:

+----------------------------------------------+---------------------------------------------------+
|Aplicaciones (QGIS Desktop, QGIS Server)      | https://issues.qgis.org/projects/qgis/issues      |
+----------------------------------------------+---------------------------------------------------+
|`Sitio web de QGIS <https://qgis.org>`_       |  https://github.com/qgis/QGIS-Website/issues      |
+----------------------------------------------+---------------------------------------------------+
|`Documentación QGIS <https://docs.qgis.org>`_ | https://github.com/qgis/QGIS-Documentation/issues |
+----------------------------------------------+---------------------------------------------------+

En el primer caso, para informar de un problema de QGIS o de algún complemento del núcleo es preciso disponer de
una `cuenta en OSGeo <https://www.osgeo.org/cgi-bin/ldap_create_user.py>`_.
Para los otros dos casos será necesario disponer de una `cuenta de GitHub <https://github.com/join>`_.

Los enlaces para reportar errores de complementos externos de terceros se pueden localizar en el
Administrador de Complementos de QGIS.

Blogs y foros
-------------

Otros idiomas
^^^^^^^^^^^^^

* `QGIS.org blog <http://blog.qgis.org/>`_: Blog oficial de QGIS.

* `QGIS Planet <https://plugins.qgis.org/planet/>`_: Incluye entradas de múltiples Blogs.

* `Planet OSGeo <http://planet.osgeo.org/>`_: Planet OSGeo es una ventana al mundo, el trabajo y las vidas de los
  miembros de OSGeo, hackers y colaboradores. Se agregan además Blogs de terceros.

* `Blog de OPENGIS.ch <http://www.opengis.ch/tech-blog/>`_: Interesante Blog de los desarrolladores de QGIS para Android
  y QField para QGIS

* `Blog del grupo de usuarios QGIS UK <https://ukqgis.wordpress.com/>`_: El Grupo de Usuarios QGIS del Reino Unido
  se creó en 2013 para proporcionar un foro donde los usuarios de QGIS del Reino Unido puedan compartir información
  y experiencias de QGIS y otros recursos de SIG de código abierto.

* `How to in QGIS <https://howtoinqgis.wordpress.com/>`_: Blog how to de QGIS a nivel usuario.

* `Spatial Galaxy <http://spatialgalaxy.net/>`_: Blog de Gary Sherman sobre GIS open source, QGIS, PyQGIS, Python,
  programación, etc. en el ámbito geoespacial.

* `Free and Open Source GIS Ramblings <https://anitagraser.com/>`_: Blog de Anita Graser, formó parte del Comité
  Directivo del Proyecto QGIS y de la Junta Directiva de OSGeo. Tiene numerosas publicaciones sobre QGIS.

* `nyalldawson.net <http://nyalldawson.net/>`_: Mapping, GIS, QGIS & MapBasic.

* `Blog Lutra consulting <https://www.lutraconsulting.co.uk/blog/>`_: Lutra Consulting brinda servicios de consultoría,
  migración, desarrollo de software, capacitación y soporte comercial para QGIS y otros proyectos SIG de código abierto.

* `Blog Nathen Woodrow <https://nathanw.net/>`_: QGIS Developer, Python (Monty and code) fan. A blog mostly about QGIS
  stuff, but not always.

* `Blog Kartoza <http://kartoza.com/en/blog/>`_: Blog de Tim Sutton. Anterior Linfiniti Geo Blog http://linfiniti.com/

* `Blog de Anderson Maciel Lima de Medeiros <http://www.andersonmedeiros.com/>`_: Blog brasileño del ganador del mejor
  twitter Geo de 2012 en MundoGEO#Connect LatinAmerica 2012: @clickgeo

* `QGIS tutorials and tips <http://www.qgistutorials.com/en/>`_: Blog de Ujaval Gandhi. Ver Python Scripting (PyQGIS).

* `Blog Oslandia <https://oslandia.com/en/blog/>`_: Blog de Oslandia, empresa privada creada por expertos en SIG y
  datos espaciales.


Castellano
^^^^^^^^^^

Canales de YouTube
------------------

Otros recursos
--------------

Python
======

Qt
==



Libros de referencia
********************
