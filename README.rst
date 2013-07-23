=============================
A Lot of Effort
=============================

.. image:: https://badge.fury.io/py/alotofeffort.png
    :target: http://badge.fury.io/py/alotofeffort
    
.. image:: https://travis-ci.org/audreyr/alotofeffort.png?branch=master
        :target: https://travis-ci.org/audreyr/alotofeffort

.. image:: https://pypip.in/d/alotofeffort/badge.png
        :target: https://crate.io/packages/alotofeffort?version=latest

Instantly deploy static HTML sites to S3 at the command line.

I created this out of frustration, after spending a lot of effort trying to
find a PyPI package that did this without problems.

Documentation
-------------

The full documentation is at http://alotofeffort.rtfd.org.

Quickstart
----------

Install it::

    pip install alotofeffort
    
Configure Boto the standard way in `~/.boto`::

    [Credentials]
    aws_access_key_id = ...
    aws_secret_access_key = ...

Then use it to deploy a static HTML website to an S3 bucket::

	$ alotofeffort www/ mybucket

Features
--------

* Uses standard Boto configuration.
* Prints the S3 endpoint URL after deploying.
* Auto-configures the bucket to be a website, with all files public.
