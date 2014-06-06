#!/usr/bin/env python
'''
The setup script for SaltTesting
'''

import os
import sys

SETUP_KWARGS = {}
USE_SETUPTOOLS = False

if 'USE_SETUPTOOLS' in os.environ:
    try:
        from setuptools import setup
        USE_SETUPTOOLS = True

        if sys.version_info < (2, 7):
            SETUP_KWARGS['install_requires'] = ['unittest2', 'argparse']
        SETUP_KWARGS['entry_points'] = {
            'console_scripts': [
                'salt-runtests = salttesting.runtests:main'
            ]
        }
    except ImportError:
        USE_SETUPTOOLS = False


if USE_SETUPTOOLS is False:
    from distutils.core import setup
    SETUP_KWARGS['scripts'] = ['scripts/salt-runtests']

exec(
    compile(
        open('salttesting/version.py').read(), 'salttesting/version.py', 'exec'
    )
)


NAME = 'SaltTesting'
VERSION = __version__
DESCRIPTION = (
    'Required testing tools needed in the several SaltStack projects.'
)

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author='Pedro Algarvio',
    author_email='pedro@algarvio.me',
    url='http://saltstack.com',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
    ],
    packages=[
        'salttesting',
        'salttesting/ext',
        'salttesting/parser',
        'salttesting/pylintplugins',
    ],
    **SETUP_KWARGS
)
