=============================
A Lot of Effort
=============================

.. image:: https://img.shields.io/pypi/v/alotofeffort.svg?style=flat
        :target: https://pypi.python.org/pypi/alotofeffort

.. image:: https://img.shields.io/travis/audreyr/alotofeffort.svg
        :target: https://travis-ci.org/audreyr/alotofeffort

Instantly deploy static HTML sites to S3 at the command line.

I created this out of frustration, after spending a lot of effort trying to
find a PyPI package that did this without problems.

Documentation
-------------

The full documentation is at https://alotofeffort.readthedocs.io.

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
* Only files that have changed get uploaded. Files are checked for changes by
  comparing the local and remote MD5 hashes of the files.
* Never auto-deletes. In fact, it doesn't delete files at all! (In the future,
  it will check if any files need to be deleted from S3, and prompt you before
  deleting anything.)
