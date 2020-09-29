Título principal de la página
=============================
https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html
https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

Links to study
--------------
`SARbian OS <https://eo-college.org/sarbian/#intro>`_: An easy-to-use Linux-based SAR processing operating system

Título 2
~~~~~~~~

Título 3
^^^^^^^^

Título 4
""""""""


Este es un párrafo.

Este es otro párrafo.

**negrita**, *cursiva*,
``código``.



`Git <https://git-scm.com>`_

https://www.python.org/


`Sphinx`__

__ http://www.sphinx-doc.org

.. figure:: _static/imagenes/avatar.png
    :width: 100
    :alt: Alternative text
    :align: right




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

.. _making-links:

Making links
============

It is easy to make a link to `yahoo <http://yahoo.com>`_ or to some
section inside this document (see ) or another
document.