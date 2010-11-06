
Overview
========

This is a simple ``zc.buildout`` recipe to to synchronize data
from one place to another. It can be used to transfer 
a ZODB ``Data.fs`` file from production to development.

It assumes you have a UNIX-based operating system, and that
the ``rsync`` binary is in your path when you run ``Buildout``.

Supported options
-----------------

This recipe supports the following options:

+-------+--------------------------------------------------------------------+
|source |The source argument to pass to rsync                                |
+-------+--------------------------------------------------------------------+
|target |The destination argument to pass to rsync                           |
+-------+--------------------------------------------------------------------+

Example usage
-------------

Here is an example ``database.cfg`` file::

    [buildout]
    extends = buildout.cfg
    parts += database

    [database]
    recipe = collective.recipe.rsync
    source = user@host.com:/srv/plone/var/filestorage/Data.fs
    target = var/filestorage/Data.fs

Then when you run Buildout you should see something like this::

    $ bin/buildout -c database.cfg
    ...
    --------------------------------------------------------------------------------
    Running rsync...
      rsync -av --partial --progress
    client.com:/srv/client/var/filestorage/Data.fs
    /Users/aclark/Developer/Products.client/var/filestorage
      this may take a while!

Contact
-------

- Questions and comments to aclark@aclark.net.
- Report bugs to aclark@aclark.net.
