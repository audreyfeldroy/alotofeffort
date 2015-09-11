#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import logging
import os
import socket

import boto
from boto.s3.key import Key


logger = logging.getLogger(__name__)


def deploy_file(file_path, bucket):
    """ Uploads a file to an S3 bucket, as a public file. """

    # Paths look like:
    #  index.html
    #  css/bootstrap.min.css

    logger.info("Deploying {0}".format(file_path))

    # Upload the actual file to file_path
    k = Key(bucket)
    k.key = file_path
    try:
        k.set_contents_from_filename(file_path)
        k.set_acl('public-read')
    except socket.error:
        logger.warning("Caught socket.error while trying to upload {0}".format(file_path))
        logger.warning("Please file an issue with alotofeffort if you see this,")
        logger.warning("providing as much info as you can.")


def deploy(www_dir, bucket_name):
    """ Deploy to the configured S3 bucket. """

    # Set up the connection to an S3 bucket.
    conn = boto.connect_s3()
    bucket = conn.get_bucket(bucket_name)

    # Deploy each changed file in www_dir
    os.chdir(www_dir)
    for root, dirs, files in os.walk('.'):
        for f in files:
            # Use full relative path. Normalize to remove dot.
            file_path = os.path.normpath(os.path.join(root, f))

            if has_changed_since_last_deploy(file_path, bucket):
                deploy_file(file_path, bucket)
            else:
                logger.info("Skipping {0}".format(file_path))

    # Make the whole bucket public
    bucket.set_acl('public-read')

    # Configure it to be a website
    bucket.configure_website('index.html', 'error.html')

    # Print the endpoint, so you know the URL
    logger.info("Your website is now live at {0}".format(bucket.get_website_endpoint()))
    logger.info("If you haven't done so yet, point your domain name there!")


def has_changed_since_last_deploy(file_path, bucket):
    """
    Checks if a file has changed since the last time it was deployed.

    :param file_path: Path to file which should be checked. Should be relative
                      from root of bucket.
    :param bucket_name: Name of S3 bucket to check against.
    :returns: True if the file has changed, else False.
    """

    logger.debug("Checking if {0} has changed since last deploy.".format(file_path))
    with open(file_path) as f:
        data = f.read()
        file_md5 = hashlib.md5(data.encode('utf-8')).hexdigest()
        logger.debug("file_md5 is {0}".format(file_md5))

    key = bucket.get_key(file_path)

    # HACK: Boto's md5 property does not work when the file hasn't been
    # downloaded. The etag works but will break for multi-part uploaded files.
    # http://stackoverflow.com/questions/16872679/how-to-programmatically-
    #     get-the-md5-checksum-of-amazon-s3-file-using-boto/17607096#17607096
    # Also the double quotes around it must be stripped. Sketchy...boto's fault
    if key:
        key_md5 = key.etag.replace('"', '').strip()
        logger.debug("key_md5 is {0}".format(key_md5))
    else:
        logger.debug("File does not exist in bucket")
        return True

    if file_md5 == key_md5:
        logger.debug("File has not changed.")
        return False
    logger.debug("File has changed.")
    return True
