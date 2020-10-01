https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html
https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

Jerarquía Sections
==================
= - _ * + #

# with overline, for parts

* with overline, for chapters

=, for sections

-, for subsections

^, for subsubsections

", for paragraphs

Hiperlinks
----------
Formas de crear hiperenlaces

    `title <link>`_

Este es un párrafo.

Este es otro párrafo.

**negrita**, *cursiva*,
``código``.

Grid tables
-----------
+--------------+----------+-----------+-----------+
| row 1, col 1 | column 2 | column 3  | column 4  |
+--------------+----------+-----------+-----------+
| row 2        |  Use the command ``ls | more``.  |
+--------------+----------+-----------+-----------+
| row 3        |          |           |           |
+--------------+----------+-----------+-----------+

+--------------+----------+-----------+-----------+
| row 1, col 1 | column 2 | column 3  | column 4  |
+--------------+----------+-----------+-----------+
| row 2        |                                  |
+--------------+----------+-----------+-----------+
| row 3        |          |           |           |
+--------------+----------+-----------+-----------+

Simple table
------------
=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======

+----------------------------------------------------------------------------------------------------------------------+
| De forma genérica y en este contexto, los **manuales de usuario** (*user guide*) son utilizados para describir las   |
| características y funcionalidades disponibles en una determinada aplicación informática y su forma de uso.           |
| Los manuales de usuario explican todas las pantallas y campos.                                                       |
| Un **manual de aprendizaje** (*training manual*) se redacta de forma diferente y puede estar acompañado de ejercicios|
| para que el usuario los complete. Describen una parte específica del sistema, paso a paso, pero no explican todas    |
| las funcionalidades y características de la herramienta informática. Suelen tener más capturas de pantallas          |
| que los manuales de usuario.                                                                                         |
+----------------------------------------------------------------------------------------------------------------------+

::

  Lo que escribo acá se ve como código fuente.

* Elemento 1

* Elemento 2

  * Elemento 2.1

* Elemento 3


******************
Sphinx cheat sheet
******************

Here is a quick and dirty cheat sheet for some common stuff you want
to do in sphinx and ReST.  You can see the literal source for this


.. _formatting-text:

Formatting text
===============

You use inline markup to make text *italics*, **bold**, or ``monotype``.

You can represent code blocks fairly easily::

   import numpy as np
   x = np.random.rand(12)

Or literally include code:

.. _making-a-table:

Making a table
==============

This shows you how to make a table -- if you only want to make a list see :

==================   ============
Name                 Age
==================   ============
John D Hunter        40
Cast of Thousands    41
And Still More       42
==================   ============

Otra tabla

============  ===========
**Servicio**  Descripcion
------------  -----------
hola          dami
============  ===========



