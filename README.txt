
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
|source |The source argument to pass to rsync, e.g.                          |
|       |user@somehost.com:/srv/client/var/filestorage/Data.fs               |
+-------+--------------------------------------------------------------------+
|target |The destination argument to pass to rsync, e.g.                     |
|       |${buildout:directory}/var/filestorage/Data.fs                       |
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

Contact
-------

- Questions and comments to aclark@aclark.net.
- Report bugs to aclark@aclark.net.
