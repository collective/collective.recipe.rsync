Changelog
---------

2.3.0 (2019-03-21)
~~~~~~~~~~~~~~~~~~

- Python 3 fix [petschki]

2.2.2 (2014-02-23)
~~~~~~~~~~~~~~~~~~

- Bug fix: provide all parameters to script option unless None

2.2.1 (2014-02-23)
~~~~~~~~~~~~~~~~~~

- Bug fix: provide all parameters to script option

2.2.0 (2014-02-23)
~~~~~~~~~~~~~~~~~~

- Add ``exclude`` support

- None have quote around when script option is use and port is not in use. Fixes #3
  [bsuttor]

2.1.0 (2012-04-09)
~~~~~~~~~~~~~~~~~~

- Clean up package

2.0.0 (2011-05-24)
~~~~~~~~~~~~~~~~~~

- Don't prefix scripts with "rsync-"

1.9 (2011-04-12)
~~~~~~~~~~~~~~~~

- Call install on update
- UI tweaks

1.8 (2011-03-29)
~~~~~~~~~~~~~~~~

- Switched to using subprocess to call rsync (to show progress to stdout)
  [mattss]

- Replace print statements with logger

- Update docs

1.7 (2011-01-21)
~~~~~~~~~~~~~~~~

-  Doc fixes
-  Make script name based on section name

  - Support more than one script in the same buildout

1.6 (2011-01-20)
~~~~~~~~~~~~~~~~

-  Add ``script`` option

  - Generates bin/rsync script
  - Disables rsync during buildout execution
  - Facilitates creation of scheduled rsyncs via cron

1.5 (2011-01-10)
~~~~~~~~~~~~~~~~

- Add a note about UNIX compat only

1.4 (2011-01-10)
~~~~~~~~~~~~~~~~

- Support alternate ssh ``port`` parameter in recipe section. This allows ``collective.recipe.rsync`` to execute rsync with: -e 'ssh <port>', which facilitates copying over non-standard ssh ports.

1.3 (2010-12-19)
~~~~~~~~~~~~~~~~

- Fix docs

1.2 (2010-12-19)
~~~~~~~~~~~~~~~~

- Fix docs
- Add new test harness
- Clean up package

1.1 (2010-11-05)
~~~~~~~~~~~~~~~~

- Modified output to include rsync command line being executed

1.0 (2010-02-28)
~~~~~~~~~~~~~~~~

- Rename package from collective.recipe.rsync_datafs to collective.recipe.rsync

0.1 (2009-08-26)
~~~~~~~~~~~~~~~~

- Created recipe with ZopeSkel
