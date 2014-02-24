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


def rsync(exclude=None, port=None, rsync_options=None, source=None, target=None):
    """
    Parse options, build and run command
    """

    # Parse options
    if rsync_options is None:
        rsync_options = OPTIONS.split()
    else:
        rsync_options = rsync_options.split()
    if exclude:
        for e in exclude.split():
            rsync_options += ['--exclude=%s' % e]
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
        'Note: depending on size & location of source file(s),'
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
        self.exclude = None
        self.port = None
        self.rsync_options = None
        self.script = False
        if 'exclude' in self.options:
            self.exclude = options['exclude']
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
            arguments = ''
            for key, value in {'exclude': self.exclude, 'rsync_options': self.rsync_options, 'port': self.port, 'source': self.source, 'target': self.target}.iteritems():
                if value is not None:
                    arguments += "%s='%s', " % (key, value)
            create_script(
                [
                    (
                        '%s' % self.name,
                        'collective.recipe.rsync.__init__', 'rsync')
                ],
                working_set,
                executable,
                bindir,
                arguments=arguments)
            return tuple()
        else:
            # if we make it this far, script option is not set so we execute
            # as buildout runs
            rsync(
                exclude=self.exclude,
                port=self.port,
                rsync_options=self.rsync_options,
                source=self.source,
                target=self.target,
                )
            return tuple()

    def update(self):
        """
        """
        self.install()
