#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_send
------------

Tests for `alotofeffort.send` module.
"""

import os
import shutil
import unittest

import boto
from boto.s3.key import Key

from alotofeffort.send import has_changed_since_last_deploy


@unittest.skip(reason='Only works with a real S3 account, which costs money.')
class IntegrationTestSend(unittest.TestCase):
    
    def setUp(self):
        self.conn = boto.connect_s3()
        self.bucket = self.conn.create_bucket('test_bucket_alotofeffort')
        self.file_path='tests/files/index.html'

    def test_has_changed_since_last_deploy_new(self):
        result = has_changed_since_last_deploy(
            file_path=self.file_path,
            bucket=self.bucket
        )
        self.assertTrue(result)

    def test_has_changed_since_last_deploy_old_unchanged(self):
        k = Key(self.bucket)
        k.key = self.file_path
        k.set_contents_from_filename(self.file_path)
    
        result = has_changed_since_last_deploy(
            file_path=self.file_path,
            bucket=self.bucket
        )
        self.assertFalse(result)
        
        # Cleanup
        k.delete()

    def tearDown(self):
        self.conn.delete_bucket('test_bucket_alotofeffort')
        
        
if __name__ == '__main__':
    unittest.main()
