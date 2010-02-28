# -*- coding: utf-8 -*-
"""Recipe rsync_datafs"""

from commands import getoutput

class Recipe(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options
        source=options['source'] 
        target=options['target']
        print 'Rsyncing data… this could take a while!'
        print(getoutput('rsync -av --partial --progress %s %s' % (source,target)))

    def install(self):
        """Installer"""
        # XXX Implement recipe functionality here

        # Return files that were created by the recipe. The buildout
        # will remove all returned files upon reinstall.
        return tuple()

    def update(self):
        """Updater"""
        pass
