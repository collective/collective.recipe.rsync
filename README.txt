.. contents::

- Code repository: http://svn.plone.org/svn/collective/buildout/collective.recipe.rsync_datafs/
- Questions and comments to aclark@aclark.net.
- Report bugs to aclark@aclark.net.

Overview
========

This is a simple zc.buildout recipe to to synchronize data 
from one place to another. Typically, it is used to transfer 
a Zope Data.fs file from production to development.

It assumes you have a UNIX-based operating system and that
the rsync binary is in your path when you run buildout.

