==========================
Blog du Capitole du Libre
==========================

Le site utilise pelican pour générer les pages HTML à partir de fichiers en rst.

Il suffit d'installer pelican dans un virtualenv en local pour générer le site entier, il n'est pas utile de l'installer sur le serveur.

Installation
=============

Prérequis
---------

::

    sudo apt-get install curl python python-virtualenv make

Installation
------------

Installer Pelican dans un virtualenv comme indiqué dans `la documentation de Pelican <http://docs.getpelican.com/en/3.6.0/install.html>`_

Installer les dépendances nécessaires::

    pip install -r requirements.txt

Cloner le repository
--------------------

::

    git clone https://github.com/toulibre/cdl-blog.git

Lier le thème dans système de fichiers
--------------------------------------

::

    cd cdl-blog
    pelican-themes -s cdltheme-blog

Utilisation
=============

Avant de lancer les commandes pour générer les pages, source le virtualenv ::

    source bin/activate

Générer le site en local
-------------------------

Générer le site à l'aide du script de développement :

::

    cd cdl-blog
    make clean
    make devserver

Puis visiter la page http://localhost:8000/ pour visualiser le site.

Mettre en ligne le site
-------------------------

Pour envoyer les fichiers situés dans "output" sur le serveur, vous pouvez
vous aider de la commande

::

    make rsync_upload

Cette commande génère le site avec les paramètres pour la version de
production, puis synchronise les fichiers avec le serveur.

Les paramètres de connexion sont dans le fichier Makefile, il faut une clé
ssh pour se connecter au serveur bien sûr :-)

Édition
--------

En savoir plus sur l'`édition des pages et du blog`_ du site du Capitole du Libre.

.. _`édition des pages et du blog`: docs/edition.rst
