.. contents::

Introduction
============

``collective.recipe.rsync`` is a ``zc.buildout`` recipe that copies
files between two places via the ``rsync`` program. 

It was originally created to copy a ``Data.fs`` file between two Plone
environments (from production to development). But
you can use it to copy any file or set of files; e.g. ZODB blob files, and so on.

.. Note::

    ``collective.recipe.rsync`` currently assumes you have a UNIX-based
    operating system and that the ``rsync`` binary is in your path when you
    execute buildout or the rsync script.

Installation
------------

Add a section to your ``buildout.cfg`` file, e.g. ``filestorage``::

    [buildout]
    parts =
        ...
        filestorage

    [filestorage]
    recipe = collective.recipe.rsync
    source = aclark@aclark.net:/srv/aclark/var/filestorage/Data.fs
    target = var/filestorage/Data.fs

Run buildout; you should see:: 

    Running rsync...
      rsync -av --partial --progress
    aclark@aclark.net:/srv/aclark/var/filestorage/Data.fs
    var/filestorage/Data.fs
      this may take a while!
    ...

Specify alternate SSH port
~~~~~~~~~~~~~~~~~~~~~~~~~~

Optionally, you may specify an alternate SSH port for ``rsync`` to use::

    [filestorage]
    recipe = collective.recipe.rsync
    source = aclark@aclark.net:/srv/aclark/var/filestorage/Data.fs
    target = var/filestorage/Data.fs
    port = 22001

Run buildout; you should see:: 

    Running rsync...
      rsync -e 'ssh -p 22001' -av --partial --progress 
    aclark@aclark.net:/srv/aclark/var/filestorage/Data.fs
    var/filestorage/Data.fs
      this may take a while!
    ...

Create a script
~~~~~~~~~~~~~~~

Optionally, you may create a ``rsync`` script to execute later. Just configure ``script = true`` like so::

    [sample]
    recipe = collective.recipe.rsync
    source = sample_input.txt
    target = sample_input_copy.txt
    script = true

Run buildout; you should see:: 

    $ bin/buildout
    ...
    Installing sample.
    Generated script '/Users/aclark/Developer/collective/collective.recipe.rsync/bin/rsync-sample'.

Notice that ``rsync`` is no longer executed when you run buildout. You may now run
the ``rsync`` script whenever you like::

    $ bin/rsync-sample
    ...
    Running rsync...
      rsync -e 'ssh -p None' -av --partial --progress sample_input.txt
    sample_input_copy.txt
      this may take a while!
    ...

Further, you may now execute an ``rsync`` script automatically via cron
(see: http://pypi.python.org/pypi/z3c.recipe.usercrontab).

Example
-------

Here are the contents of a sample ``database.cfg`` file; this example demonstrates how to copy a
``Data.fs`` file and ``var/blobstorage`` files::

    [buildout]
    extends = buildout.cfg
    parts += 
        filestorage
        blobstorage

    [filestorage]
    recipe = collective.recipe.rsync
    source = aclark.net:/srv/aclark_net_website/var/filestorage/Data.fs
    target = var/filestorage/Data.fs

    [blobstorage]
    recipe = collective.recipe.rsync
    source = aclark.net:/srv/aclark_net_website/var/blobstorage/
    target = var/blobstorage


Contact
-------

Questions/comments/concerns? Please e-mail: aclark@aclark.net.

