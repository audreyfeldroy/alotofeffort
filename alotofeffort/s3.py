#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import boto
from boto.s3.key import Key

def get_bucket_name():
    try:
        bucket_name = os.environ.get('ALOTOFEFFORT_BUCKET')
    except KeyError:
        print("Please set the ALOTOFEFFORT_BUCKET environment variable.")
    return bucket_name
    
def setup_connection():
    """ Set up the connection to an S3 bucket. """
    conn = boto.connect_s3()
    bucket_name = get_bucket_name()
    bucket = conn.get_bucket(bucket_name)

def deploy():
    """ Deploy to the configured S3 bucket. """

    # Put together HTML page content as string
    content = '<a href="{0}">{0}</a>'.format(args.url)

    # Upload index.html to the bucket as public file
    k = Key(bucket)
    k.key = 'index.html'
    k.set_metadata("Content-Type", 'text/html')
    k.set_contents_from_string(content)
    k.make_public()
