# -*- coding: utf-8 -*-
"""Recipe rsync"""

import logging
import sys
import subprocess
from pkg_resources import working_set
from sys import executable
from zc.buildout.easy_install import scripts as create_script

_LOG = logging.getLogger("rsync")
line = ('-----------------------------------' +
        '-----------------------------------')

def rsync(source=None, target=None, port=None):
    if port:
        cmd = ['rsync', '-e', 'ssh -p %s' % port, '-av', '--partial',
            '--progress', source, target]
    else:
        cmd = ['rsync', '-av', '--partial', '--progress', source, target]
    _LOG.info(line)
    _LOG.info('Running rsync with command: ')
    _LOG.info('  $ %s' % ' '.join(cmd))
    _LOG.info('  Note: depending on the source file(s) size and location, this may take a while!')
    _LOG.info(line)
    subprocess.call(cmd)
    _LOG.info('Done.')


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


    def install(self):
        """Installer"""
        if self.script:
            bindir = self.buildout['buildout']['bin-directory']
            arguments = "source='%s', target='%s', port='%s'"
            create_script(
                [('%s' % self.name, 'collective.recipe.rsync.__init__', 'rsync')],
                working_set, executable, bindir, arguments=arguments % (
                self.source, self.target, self.port))
            return tuple((bindir + '/' + 'rsync',))
        else:
            # if we make it this far, script option is not set so we execute
            # as buildout runs
            rsync(source=self.source, target=self.target, port=self.port)
            return tuple()

    def update(self):
        """Updater"""
        self.install()
