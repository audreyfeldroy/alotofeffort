#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = ['boto==2.38.0']

if sys.version_info[:2] < (2, 7):
    requirements.append('argparse')

setup(
    name='alotofeffort',
    version='0.4.1',
    description='Deploy static HTML sites to S3 at the command line.',
    long_description=readme + '\n\n' + history,
    author='Audrey Roy',
    author_email='audreyr@gmail.com',
    url='https://github.com/audreyr/alotofeffort',
    packages=[
        'alotofeffort',
    ],
    package_dir={'alotofeffort': 'alotofeffort'},
    entry_points={
        'console_scripts': [
            'alotofeffort = alotofeffort.main:main',
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='alotofeffort',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
)
