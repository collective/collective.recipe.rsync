.. contents::

Introduction
============

``collective.recipe.rsync`` is a ``zc.buildout`` recipe that copies a
file (or files) between two locations via the ``rsync`` program. 

It was originally created to make it easy to copy a ``Data.fs`` file
between two Plone application environments e.g. from production to
development, but you can use it to copy anything; e.g. ZODB blob files,
and so on.

.. Note::

    ``collective.recipe.rsync`` currently assumes you have a UNIX-based
    operating system and that the ``rsync`` binary is in your path when
    you execute buildout or the rsync script. Windows testers are welcome.

Installation
------------

Add a section to your ``buildout.cfg`` file, e.g. ``data``::

    [buildout]
    parts =
        ...
        data

    [data]
    recipe = collective.recipe.rsync
    source = myhost.com:/path/to/Data.fs
    target = var/filestorage/Data.fs

This copies a Data.fs file from myhost.com to ./var/filestorage/Data.fs.

Specify alternate SSH port
~~~~~~~~~~~~~~~~~~~~~~~~~~

Optionally, you may specify an alternate SSH port for ``rsync`` to use::

    [data]
    recipe = collective.recipe.rsync
    source = myhost.com:/path/to/Data.fs
    target = var/filestorage/Data.fs
    port = 22001

This copies a Data.fs file from myhost.com to ./var/filestorage/Data.fs over
port 22001.

Create a script
~~~~~~~~~~~~~~~

Normally, ``collective.recipe.rsync`` will run ``rsync`` during the recipe
installation. Optionally, you can create a script to execute ``rsync`` later
by configuring the ``script = true`` option::

    [data]
    recipe = collective.recipe.rsync
    source = myhost.com:/path/to/Data.fs
    target = var/filestorage/Data.fs
    script = true

This is useful in cases where you want to automate an ``rsync`` process with
cron e.g. via http://pypi.python.org/pypi/z3c.recipe.usercrontab.

Example
-------

Here is a real life example. This is one of the ways in which the author uses
``collective.recipe.rsync``::

    # Create scripts to deploy staging data to production.
    # Be VERY careful with this. You could easily overwrite your
    # live production data if you either forget to use the script
    # option, or accidentally run the bin/rsync-filestorage-to-production
    # script without stopping the production site first.
    [filestorage-to-production]
    recipe = collective.recipe.rsync
    source = var/filestorage/Data.fs
    target = ../aclark_net_website/var/filestorage/Data.fs
    script = true

    [blobstorage-to-production]
    recipe = collective.recipe.rsync
    source = var/blobstorage/
    target = ../aclark_net_website/var/blobstorage/
    script = true

As the warning suggests, you should be careful with this. The author uses this
particular configuration to deploy a staging site to production.

Contact
-------

Questions/comments/concerns? E-mail: aclark@aclark.net.
