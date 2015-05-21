
===============
Leonardo Stores
===============

Physical store integration for Leonardo Ecommerce.

* A store locator page using Google maps for geocoding. It also supports using the browser's location to show the nearest stores.
* Store detail pages including opening hours
* Store groups

Integration Oscar Stores see https://github.com/django-oscar/django-oscar-stores

.. contents::
    :local:

Dependencies
------------

GeoDjango_ is used so a spatial database is required.  We recommend PostGIS.
Django's docs include some `installation instructions`_ although it is renowned
for being tricky.

.. _GeoDjango: https://docs.djangoproject.com/en/1.4/ref/contrib/gis
.. _`installation instructions`: https://docs.djangoproject.com/en/1.4/ref/contrib/gis/install

Spatialite is another option although it can be tricky to set up.  On Ubuntu,
you can do the following:

.. code:: bash

    $ sudo apt-get install spatialite-bin libspatialite3 libgeos++-dev libgdal-dev libproj0

The ``pysqlite`` python package is also required although it doesn't support C
extensions by default.  To work-around this, there are two options:

1. Download the package, edit ``setup.cfg`` to enable C extensions and install:

.. code:: bash

    $ pip install pysqlite --no-install
    $ vim $VIRTUAL_ENV/build/pysqlite/setup.cfg
    $ pip install pysqlite

2. Use a custom branch:

.. code:: bash

   $ pip install git+git://github.com/tinio/pysqlite.git@extension-enabled#egg=pysqlite

.. _`pysqlite`: http://code.google.com/p/pysqlite

Installation
------------

.. code-block:: bash

    pip install leonardo-module-eshop[stores]

Configuration
-------------

Add ``eshop_stores`` to leonardo APPS list, in the ``local_settings.py``::

    APPS = [
        ...
        'eshop_stores',
        ...
    ]

    STORES_GEOGRAPHIC_SRID = 3577  # This is used for distance calculations. See http://spatialreference.org for more details.
    STORES_GEODETIC_SRID = 4326
    STORES_MAX_SEARCH_DISTANCE = None  # This filters stores in queries by distance. Units can be set using distance object:

Read More
=========

* https://github.com/django-oscar
* https://github.com/django-leonardo
* https://github.com/leonardo-modules/leonardo-store
