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
        if 'port' in options:
            port = options['port']
            self.rsync(source, target, port=port)
        else:
            self.rsync(source, target, port=None)

    def rsync(self, source, target, port=None)
        if port:
            cmd = "  rsync -e 'ssh -p %s' -av --partial --progress %s %s" % (
                port, source, target)
        else:
            cmd = '  rsync -av --partial --progress %s %s' % (source, target)

        print line
        print 'Running rsync...'
        print cmd
        print '  this may take a while!'
        print getoutput(cmd)
        print 'Done.'
        print line


    def install(self):
        """Installer"""
        # XXX Implement recipe functionality here

        # Return files that were created by the recipe. The buildout
        # will remove all returned files upon reinstall.

        # http://pypi.python.org/pypi/zc.buildout#the-scripts-function
        create_scripts([('rsync', '__init__', 'rsync')],
            working_set, executable, bindir, arguments=None)

        bindir = self.buildout['buildout']['bin-directory']
        return tuple((bindir + '/' + 'rsync',))


    def update(self):
        """Updater"""
        pass
