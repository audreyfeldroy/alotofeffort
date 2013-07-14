#!/usr/bin/env python

import os
import sys

import alotofeffort

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst', 'rt').read()
history = open('HISTORY.rst', 'rt').read()

setup(
    name='alotofeffort',
    version=alotofeffort.__version__,
    description='Deploy static HTML sites to S3 with the simple "alotofeffort" command.',
    long_description=readme + '\n\n' + history,
    author='Audrey Roy',
    author_email='audreyr@gmail.com',
    url='https://github.com/audreyr/alotofeffort',
    packages=[
        'alotofeffort',
    ],
    include_package_data=True,
    install_requires=[
    ],
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
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)