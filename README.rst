Introduction
============

``collective.recipe.rsync`` is a `zc.buildout`_ recipe that copies files between two locations via the ``rsync`` program.

.. Note::

    ``collective.recipe.rsync`` assumes you have a UNIX-based operating system and the ``rsync`` binary is in your PATH when you run Buildout or the ``rsync`` script.

Installation
------------

Add a new section to your ``buildout.cfg`` file to use the ``collective.recipe.rsync`` recipe, e.g.::

    [buildout]
    extends = https://raw.github.com/plock/pins/master/plone-4-3
    parts += backup

    [backup]
    recipe = collective.recipe.rsync
    source = ${buildout:directory}/var/filestorage/Data.fs
    target = /var/backup

This copies a Plone Data.fs file from the `source` to the `target`.

Create a script
~~~~~~~~~~~~~~~

Normally ``collective.recipe.rsync`` will run ``rsync`` during the recipe installation. Optionally you can create a script to execute ``rsync`` later by configuring the ``script = true`` option::

    [backup]
    recipe = collective.recipe.rsync
    source = ${buildout:directory}/var/filestorage/Data.fs
    target = /var/backup
    script = true

This is useful in cases where you want to automate an ``rsync`` script with cron e.g. via `z3c.recipe.usercrontab`_.

Configure options
~~~~~~~~~~~~~~~~~

The default options are ``-av --partial --progress``. Use the ``options`` parameter to change them e.g.::

    [backup]
    recipe = collective.recipe.rsync
    source = ${buildout:directory}/var/filestorage/Data.fs
    target = /var/backup
    # Omit "-v" option
    options = -a --partial --progress

Exclude files
~~~~~~~~~~~~~

You can exclude files with the ``exclude`` option e.g.::

    [backup]
    recipe = collective.recipe.rsync
    source = ${buildout:directory}/var/filestorage/Data.fs
    target = /var/backup
    exclude = Data.fs.index Data.fs.old

Specify alternate SSH port
~~~~~~~~~~~~~~~~~~~~~~~~~~

Optionally you may specify an alternate SSH port for ``rsync`` to use::

    [backup]
    recipe = collective.recipe.rsync
    source = ${buildout:directory}/var/filestorage/Data.fs
    target = /var/backup
    port = 22000

This copies a Data.fs file from `remotehost` to `var/filestorage/Data.fs` using port 22000.

.. _`zc.buildout`: http://pypi.python.org/pypi/zc.buildout
.. _`z3c.recipe.usercrontab`: http://pypi.python.org/pypi/z3c.recipe.usercrontab
