# -*- coding: utf-8 -*-
from pkg_resources import working_set
from sys import executable
from zc.buildout.easy_install import scripts as create_script
import logging
import subprocess

LOG = logging.getLogger("rsync")
OPTIONS = '-av --partial --progress'

CMD = ['rsync', OPTIONS]
LINE = ('-----------------------------------' +
        '-----------------------------------')


class Recipe(object):
    """
        Buildout recipe object
    """

    def __init__(self, buildout, name, options):
        """
            Initialize class
        """
        self.buildout, self.name, self.options = buildout, name, options

        self.ignore = None
        self.port = None
        self.script = False
        self.source = options['source']
        self.target = options['target']

        if 'ignore' in options:
            self.ignore = options['ignore']
        if 'port' in options:
            self.port = options['port']
        if 'script' in options:
            if options['script'] == 'true':
                self.script = True

    def install(self):
        """
            Install recipe
        """
        if self.script:
            bindir = self.buildout['buildout']['bin-directory']
            arguments = "source='%s', target='%s', port='%s'"
            create_script([
                ('%s' % self.name, 'collective.recipe.rsync.__init__',
                    'rsync')],
                working_set, executable, bindir, arguments=arguments % (
                self.source, self.target, self.port))
            return tuple((bindir + '/' + 'rsync',))
        else:
            # if we make it this far, script option is not set so we execute
            # as buildout runs
            self.rsync()
            return tuple()

    def rsync(self):
        """
            Main routine to call rsync via subprocess module
        """
        ignore = self.ignore
        port = self.port
        source = self.source
        target = self.target

        if port:
            CMD.append('-e', 'ssh -p %s' % port)
        if ignore:
            CMD.append('-i', ignore)

        CMD.append[source, target]
        LOG.info(LINE)
        LOG.info('Running rsync with command: ')
        LOG.info('  $ %s' % ' '.join(CMD))
        LOG.info('  Note: depending on the source file(s) size and location, '
            'this may take a while!')
        LOG.info(LINE)
        subprocess.call(CMD)
        LOG.info('Done.')

    def update(self):
        """
            Call the install method on update
        """
        self.install()
