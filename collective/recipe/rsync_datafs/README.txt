Supported options
=================

The recipe supports the following options:

source
    The source argument to pass to rsync, e.g. user@remotehost.com:/srv/client/var/filestorage/Data.fs
target
    The destination argument to pass to rsync, e.g. ${buildout:directory}/var/filestorage/Data.fs

Example usage
=============

We'll start by creating a buildout that uses the recipe::

    >>> write('buildout.cfg',
    ... """
    ... [buildout]
    ... parts = database
    ...
    ... [database]
    ... recipe = collective.recipe.rsync_datafs
    ... source = %(foo)s
    ... target = %(bar)s
    ... """ % { 'foo' : 'value1', 'bar' : 'value2'})

Running the buildout gives us::

    >>> print 'start', system(buildout) 
    start...
    Installing database.
    Rsyncing data… this could take a while!
    receiving file list ... 
    1 file to consider

    sent 20 bytes  received 84 bytes  41.60 bytes/sec
    total size is 95501335  speedup is 918282.07
    Installing database.
    <BLANKLINE>
