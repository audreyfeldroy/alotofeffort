#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_s3
------------

Tests for `alotofeffort.s3` module.
"""

import os
import shutil
import unittest

import boto
from boto.s3.key import Key
from moto import mock_s3

from alotofeffort import s3


class TestS3(unittest.TestCase):

    @mock_s3
    def test_has_changed_since_last_deploy_new(self):
        conn = boto.connect_s3()
        bucket = conn.create_bucket('test_bucket')

        result = s3.has_changed_since_last_deploy(
            file_path='tests/files/index.html',
            bucket=bucket
        )
        self.assertTrue(result)

    @mock_s3
    def test_has_changed_since_last_deploy_old_unchanged(self):
        conn = boto.connect_s3()
        bucket = conn.create_bucket('test_bucket')
        file_path='tests/files/index.html'
        
        k = Key(bucket)
        k.key = file_path
        k.set_contents_from_filename(file_path)

        result = s3.has_changed_since_last_deploy(
            file_path=file_path,
            bucket=bucket
        )
        self.assertFalse(result)
        
if __name__ == '__main__':
    unittest.main()
