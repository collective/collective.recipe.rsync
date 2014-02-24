from setuptools import find_packages
from setuptools import setup
import os


VERSION = '2.2.1'


setup(
    author='Alex Clark',
    author_email='aclark@aclark.net',
    classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: Zope Public License',
    ],
    description='A zc.buildout recipe to copy files from one location\
        to another via rsync',
    entry_points={
        'zc.buildout': 'default = collective.recipe.rsync:Recipe'
    },
    include_package_data=True,
    install_requires=[
        'setuptools',
        'zc.buildout',
    ],
    keywords='plone rsync',
    license='ZPL',
    long_description=(
        open('README.rst').read() + '\n' +
        open('CHANGES.rst').read()
    ),
    name='collective.recipe.rsync',
    namespace_packages=[
        'collective',
        'collective.recipe'
    ],
    packages=find_packages(),
    test_suite='collective.recipe.rsync.tests.TestSuite',
    url='http://collective.github.com/collective.recipe.rsync',
    version=VERSION,
    zip_safe=False,
)
