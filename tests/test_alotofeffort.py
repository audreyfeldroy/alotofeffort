#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_alotofeffort
------------

Tests for `alotofeffort` module.
"""

import os
import shutil
import unittest

from alotofeffort import alotofeffort
from alotofeffort import s3


class TestALotOfEffort(unittest.TestCase):

    def test_something(self):
        """
        At least we can test which platforms this breaks on, with tox.
        """
        pass

if __name__ == '__main__':
    unittest.main()