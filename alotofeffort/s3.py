#!/usr/bin/env python

import argparse
import os
import webbrowser

import boto
from boto.s3.key import Key

# Setup
conn = boto.connect_s3()
bucket_name = os.environ.get('LINKSENDER_BUCKET')
bucket = conn.get_bucket(bucket_name)

# Get command line URL argument
parser = argparse.ArgumentParser(description='Turn a URL into a static HTML \
    link, hosted by your favorite Amazon S3 bucket.')
parser.add_argument('url', help='URL to be linked to')
args = parser.parse_args()

# TODO: use urllib or similar to avoid appending ? if it's already part of
# the entered URL.
# Get optional query component to append
query_string = os.environ.get('LINKSENDER_EXTRA_QUERY_STRING')
if query_string:
    args.url += "?" + query_string

# Put together HTML page content as string
content = '<a href="{0}">{0}</a>'.format(args.url)

# Upload index.html to the bucket as public file
k = Key(bucket)
k.key = 'index.html'
k.set_metadata("Content-Type", 'text/html')
k.set_contents_from_string(content)
k.make_public()

# Open browser to the URL
s3_url = 'http://{0}.s3-website-us-east-1.amazonaws.com'.format(bucket_name)
webbrowser.open_new(s3_url)
