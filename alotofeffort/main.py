#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import logging

from .send import deploy


def main():
    """ Entry point for the package, as defined in setup.py. """

    # Log info and above to console
    logging.basicConfig(
        format='%(levelname)s: %(message)s', level=logging.INFO)

    # Get command line input/output arguments
    msg = 'Instantly deploy static HTML sites to S3 at the command line.'
    parser = argparse.ArgumentParser(description=msg)
    parser.add_argument(
        'www_dir',
        help='Directory containing the HTML files for your website.'
    )
    parser.add_argument(
        'bucket_name',
        help='Name of S3 bucket to deploy to, e.g. mybucket.'
    )
    args = parser.parse_args()

    # Deploy the site to S3!
    deploy(args.www_dir, args.bucket_name)


if __name__ == '__main__':
    main()
