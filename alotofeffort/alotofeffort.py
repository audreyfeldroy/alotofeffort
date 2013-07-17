#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import s3

def open_url():
    """ Open browser to the URL of the freshly-deployed website. """
    s3_url = 'http://{0}.s3-website-us-east-1.amazonaws.com'.format(bucket_name)
    webbrowser.open_new(s3_url)


def main():
    """ Entry point for the package, as defined in setup.py. """
    
    # Get command line input/output arguments
    parser = argparse.ArgumentParser(
        description='Instantly deploy static HTML sites to S3 at the command line.'
    )
    parser.add_argument(
        'www_dir', 
        help='Directory containing the HTML files for your website.'
    )
    args = parser.parse_args()
    
    s3.setup_connection()
    s3.deploy(args.www_dir)


if __name__ == '__main__':
    main()
    