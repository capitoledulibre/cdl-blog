=========
Édition
=========

Architecture des pages
========================

Les fichiers source se trouvent dans le dossier ``src``, les fichiers
générés dans le dossier ``output``.

Les pages classiques sont dans le dossier ``src/pages``, mais sont générées
à la racine du dossier ``output``.

Les actualités (billets de blog) sont dans le dossier ``src/blog`` et
générées dans le dossier ``output-cdl2013/blog``.

Formats d'édition
=================

Format ``rst``
---------------

Les pages source sont au format `restructured text
<http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_

L'essentiel à savoir est qu'il faut mettre un titre principal à toute page:

::

    =================
    Titre de la page
    =================

    `Lien vers une page <http://example.com/>`_

et que les liens sont notés ```nom du lien <url>`_``

Format ``md``
---------------

Les pages source peuvent également être au format `Markdown <http://daringfireball.net/projects/markdown/>`_.

::

  # Titre de la page

  [Lien vers une page](http://example.com/ "Title")


Vous pouvez également utiliser le `convertisseur en ligne Pandoc <http://johnmacfarlane.net/pandoc/try>`_ de John Mc Farlane.
