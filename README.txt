.. contents::

- Code repository:
  http://svn.plone.org/svn/collective/buildout/collective.recipe.rsync/
- Questions and comments to aclark@aclark.net.
- Report bugs to aclark@aclark.net.

Overview
========

(Formerly collective.recipe.rsync_datafs.)

This is a simple zc.buildout recipe to to synchronize data 
from one place to another. E.g. it can be used to transfer 
a Zope Data.fs file from production to development.

It assumes you have a UNIX-based operating system, and that
the rsync binary is in your path when you run buildout.

Supported options
=================

The recipe supports the following options:

source
    The source argument to pass to rsync, e.g. user@somehost.com:/srv/client/var/filestorage/Data.fs
target
    The destination argument to pass to rsync, e.g. ${buildout:directory}/var/filestorage/Data.fs

Example usage
=============

Here we extend a buildout.cfg to add a database part::

    [buildout]
    extends = buildout.cfg
    parts += database

    [database]
    recipe = collective.recipe.rsync
    source = aclark@aclark.net:/srv/aclark/var/filestorage/Data.fs
    target = var/filestorage/Data.fs
