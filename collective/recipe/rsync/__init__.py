# -*- coding: utf-8 -*-
"""Recipe rsync"""

import subprocess
from pkg_resources import working_set
from sys import executable
from zc.buildout.easy_install import scripts as create_script


line = ('----------------------------------------' +
        '----------------------------------------')


def rsync(source=None, target=None, port=None):
    if port:
        #cmd = "  rsync -e 'ssh -p %s' -av --partial --progress %s %s" % (
        #    port, source, target)
        cmd = ["rsync", "-e", "ssh -p %s" % port, "-av", 
               "--partial", "--progress", source, target]
    else:
        cmd =["rsync", "-av", "--partial", "--progress", source, target]

    print line
    print 'Running rsync with command: \n'
    print '  $ %s\n' % ' '.join(cmd)
    print '  Note: depending on the file size, this may take a while!'
    print line
    subprocess.call(cmd)
    print 'Done.'
    print line


class Recipe(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options
        self.source = options['source']
        self.target = options['target']
        self.port = None
        self.script = False
        if 'port' in options:
            self.port = options['port']
        if 'script' in options:
            if options['script'] == 'true':
                self.script = True
                return

        # if we make it this far, script option is not set so we execute
        # as buildout runs
        rsync(source=self.source, target=self.target, port=self.port)

    def install(self):
        """Installer"""
        if self.script:
            bindir = self.buildout['buildout']['bin-directory']
            arguments = "source='%s', target='%s', port='%s'"
            create_script(
                [('rsync-%s' % self.name, 'collective.recipe.rsync.__init__', 'rsync')],
                working_set, executable, bindir, arguments=arguments % (
                self.source, self.target, self.port))
            return tuple((bindir + '/' + 'rsync',))
        else:
            return tuple()

    def update(self):
        """Updater"""
        pass
