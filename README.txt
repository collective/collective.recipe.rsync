.. contents::

Introduction
============

``collective.recipe.rsync`` is a ``zc.buildout`` recipe that makes it easy to
synchronize data between two locations, via the ``rsync`` program. 

It was originally created to make it easier to synchronize ``Data.fs``
files between production and development environments. But you can use it to 
synchronize any tree of data e.g. ZODB blob files, and so on.

Currently, it assumes you have a UNIX-based operating system and that
the ``rsync`` binary is in your path when you run buildout.

Usage
-----

Add a section to your ``buildout.cfg`` file, e.g. ``database``::

    [buildout]
    parts += database

    [database]
    recipe = collective.recipe.rsync
    source = aclark@aclark.net:/srv/aclark/var/filestorage/Data.fs
    target = var/filestorage/Data.fs

Run buildout. You should see::

    --------------------------------------------------------------------------------
    Running rsync...
      rsync -av --partial --progress
    aclark@aclark.net:/srv/aclark/var/filestorage/Data.fs
    var/filestorage/Data.fs
      this may take a while!

Contact
-------

Comments/questions/concerns? Email: aclark@aclark.net
