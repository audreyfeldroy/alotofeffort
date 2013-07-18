============
Installation
============

Install the "alotofeffort" package
----------------------------------

At the command line::

    $ easy_install alotofeffort

Or, if you have virtualenvwrapper installed::

    $ mkvirtualenv alotofeffort
    $ pip install alotofeffort
    
Configure boto
--------------

Save the following in `~/.boto`::

    [Credentials]
    aws_access_key_id = ...
    aws_secret_access_key = ...
    
Replace `...` with your AWS access credentials, of course.
