#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import socket

import boto
from boto.s3.key import Key


def deploy_file(root, f, bucket):
    """ Uploads a file to an S3 bucket, as a public file. """

    # Normalize path to remove dot
    # Paths look like:
    #  index.html
    #  css/bootstrap.min.css
    file_path = os.path.normpath(os.path.join(root, f))

    print("Deploying {0}".format(file_path))

    # Upload the actual file to file_path
    k = Key(bucket)    
    k.key = file_path
    try:
        k.set_contents_from_filename(file_path)
        k.set_acl('public-read')
    except socket.error:
        print("Caught socket.error while trying to upload {0}".format(file_path))
        print("Please file an issue with alotofeffort if you see this,")
        print("providing as much info as you can.")
    

def deploy(www_dir, bucket_name):
    """ Deploy to the configured S3 bucket. """

    # Set up the connection to an S3 bucket.
    conn = boto.connect_s3()
    bucket = conn.get_bucket(bucket_name)

    # Deploy each file in www_dir
    os.chdir(www_dir)
    for root, dirs, files in os.walk('.'):
        for f in files:
            deploy_file(root, f, bucket)

    # Make the whole bucket public
    bucket.set_acl('public-read')
    
    # Configure it to be a website
    bucket.configure_website('index.html', 'error.html')
    
    # Print the endpoint, so you know the URL
    print("Your website is now live at {0}".format(bucket.get_website_endpoint()))
    print("If you haven't done so yet, point your domain name there!")
