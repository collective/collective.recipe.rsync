Introduction
============

``collective.recipe.rsync`` is a `zc.buildout`_ recipe that copies files between two locations via the ``rsync`` program.

.. Note::

    ``collective.recipe.rsync`` currently assumes you have a UNIX-based operating system and that the ``rsync`` binary is in your path when you execute buildout or the rsync script. Ideas for Windows support are welcome.

Installation
------------

Add a section to your ``buildout.cfg`` file, e.g.::

    [buildout]
    http://build.pythonpackages.com/buildout/plone/latest
    parts += rsync

    [rsync]
    recipe = collective.recipe.rsync
    source = remotehost:/path/to/Data.fs
    target = ${buildout:directory}/var/filestorage/Data.fs

This copies a Data.fs file from `remotehost` to `var/filestorage/Data.fs` relative to the buildout root.

Specify alternate SSH port
~~~~~~~~~~~~~~~~~~~~~~~~~~

Optionally you may specify an alternate SSH port for ``rsync`` to use::

    [rsync]
    recipe = collective.recipe.rsync
    source = remotehost:/path/to/Data.fs
    target = ${buildout:directory}/var/filestorage/Data.fs
    port = 22000

This copies a Data.fs file from `remotehost` to `var/filestorage/Data.fs` using port 22000.

Create a script
~~~~~~~~~~~~~~~

Normally ``collective.recipe.rsync`` will run ``rsync`` during the recipe installation. Optionally you can create a script to execute ``rsync`` later by configuring the ``script = true`` option::

    [rsync]
    recipe = collective.recipe.rsync
    source = remotehost:/path/to/Data.fs
    target = ${buildout:directory}/var/filestorage/Data.fs
    script = true

This is useful in cases where you want to automate an ``rsync`` script with cron e.g. via `z3c.recipe.usercrontab`_.

.. _`zc.buildout`: http://pypi.python.org/pypi/zc.buildout
.. _`z3c.recipe.usercrontab`: http://pypi.python.org/pypi/z3c.recipe.usercrontab

