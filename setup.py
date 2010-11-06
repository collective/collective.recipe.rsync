# -*- coding: utf-8 -*-

###############################################################################
#                                                                             #
###############################################################################

import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.2'
long_description = (
    read('README.txt') +
    read('docs/HISTORY.txt') +
    read('docs/CONTRIBUTORS.txt'))
entry_point = 'collective.recipe.rsync:Recipe'
entry_points = {"zc.buildout": ["default = %s" % entry_point]}
tests_require = ['zope.testing', 'zc.buildout']
description = 'Buildout recipe to copy data from one place to another.'
url = 'http://svn.plone.org/svn/collective/buildout/collective.recipe.rsync/'
setup(name='collective.recipe.rsync',
      version=version,
      description=description,
      long_description=long_description,
      classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Zope Public License',
        ],
      author='Alex Clark',
      author_email='aclark@aclark.net',
      url=url,
      license='ZPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.recipe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'zc.buildout'
                        # -*- Extra requirements: -*-
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite='collective.recipe.rsync.tests.test_docs.test_suite',
      entry_points=entry_points,
      )
