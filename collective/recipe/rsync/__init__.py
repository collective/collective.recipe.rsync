# -*- coding: utf-8 -*-
import logging
import subprocess
from pkg_resources import working_set
from sys import executable
from zc.buildout.easy_install import scripts as create_script


CMD = 'rsync'
LINE = '-' * 80
LOG = logging.getLogger("rsync")
OPTIONS = '-av --partial --progress'


def rsync(rsync_options=None, source=None, target=None, port=None):
    """
    Parse options, build and run command
    """

    # Parse options
    if rsync_options is None:
        rsync_options = OPTIONS.split()
    else:
        rsync_options = rsync_options.split()
    if port:
        rsync_options += ['-e', 'ssh -p %s' % port]

    rsync_options.append(source)
    rsync_options.append(target)

    # Build cmd

    cmd = rsync_options
    cmd.insert(0, CMD)

    LOG.info(LINE)
    LOG.info('Running rsync with command: ')
    LOG.info('  $ %s' % ' '.join(cmd))
    LOG.info(
        'Note: depending on the size and location of the source file(s)'
        ' this may take a while!'
    )
    LOG.info(LINE)
    subprocess.call(cmd)
    LOG.info('Done.')


class Recipe(object):
    """
    """

    def __init__(self, buildout, name, options):
        """
        """
        self.buildout, self.name, self.options = buildout, name, options
        self.source = options['source']
        self.target = options['target']
        self.port = None
        self.rsync_options = None
        self.script = False
        if 'options' in self.options:
            self.rsync_options = options['options']
        if 'port' in options:
            self.port = options['port']
        if 'script' in options:
            if options['script'] == 'true':
                self.script = True

    def install(self):
        """
        """
        if self.script:
            bindir = self.buildout['buildout']['bin-directory']
            arguments = "source='%s', target='%s', port=%s"
            create_script(
                [
                    (
                        '%s' % self.name,
                        'collective.recipe.rsync.__init__', 'rsync')
                ],
                working_set,
                executable,
                bindir,
                arguments=arguments % (self.source, self.target, self.port))
            return tuple((bindir + '/' + 'rsync',))
        else:
            # if we make it this far, script option is not set so we execute
            # as buildout runs
            rsync(
                rsync_options=self.rsync_options,
                source=self.source,
                target=self.target,
                port=self.port)
            return tuple()

    def update(self):
        """
        """
        self.install()
