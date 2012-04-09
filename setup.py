from setuptools import find_packages
from setuptools import setup
import os

VERSION='2.0.1'


setup(
    author='Alex Clark',
    author_email='aclark@aclark.net',
    classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Zope Public License',
    ],
    description='A zc.buildout recipe to copy files from one location to another via rsync',
    entry_points={
        'zc.buildout': 'default = collective.recipe.rsync:Recipe'
    },
    include_package_data=True,
    install_requires=[
        'setuptools',
        'zc.buildout',
    ],
    license='ZPL',
    long_description=(
        open('README.rst').read() +
        open(os.path.join('docs', 'HISTORY.txt'))
    )
    name='collective.recipe.rsync',
    namespace_packages=[
        'collective',
        'collective.recipe'
    ],
    packages=find_packages(),
    url=('http://svn.plone.org/svn/collective/buildout/',
    version='2.0.0',
    zip_safe=False,
)
