# -*- coding: utf-8 -*-
"""Recipe rsync"""

from commands import getoutput
from pkg_resources import working_set
from sys import executable
from zc.buildout.easy_install import scripts as create_script


line = ('----------------------------------------' +
        '----------------------------------------')


def rsync(source=None, target=None, port=None):
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


class Recipe(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options
        self.source = options['source']
        self.target = options['target']
        if 'port' in options:
            self.port = options['port']
            rsync(source=self.source, target=self.target, port=self.port)
        else:
            rsync(source=self.source, target=self.target, port=None)

    def install(self):
        """Installer"""
        # XXX Implement recipe functionality here
        bindir = self.buildout['buildout']['bin-directory']

        # Return files that were created by the recipe. The buildout
        # will remove all returned files upon reinstall.

        arguments = "source='%s', target='%s', port='%s'"
        # http://pypi.python.org/pypi/zc.buildout#the-scripts-function
        create_script([('rsync', 'collective.recipe.rsync.__init__', 'rsync')],
            working_set, executable, bindir, arguments=arguments % (
                self.source, self.target, self.port))

        return tuple((bindir + '/' + 'rsync',))

    def update(self):
        """Updater"""
        pass
