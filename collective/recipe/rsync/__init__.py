# -*- coding: utf-8 -*-
"""Recipe rsync"""

from commands import getoutput

line = ('----------------------------------------' +
        '----------------------------------------')


class Recipe(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options
        source = options['source']
        target = options['target']

        cmd = '  rsync -av --partial --progress %s %s' % (source, target)

        if port in options:
            port = options['port']
            cmd = '  rsync -e `ssh -p %s` -av --partial --progress %s %s' % (port, source, target)

        print line
        print 'Running rsync...'
        print cmd
        print '  this may take a while!'

        print getoutput('rsync -av --partial --progress %s %s' % (
            source, target))

        print 'Done.'

        print line

    def install(self):
        """Installer"""
        # XXX Implement recipe functionality here

        # Return files that were created by the recipe. The buildout
        # will remove all returned files upon reinstall.
        return tuple()

    def update(self):
        """Updater"""
        pass
