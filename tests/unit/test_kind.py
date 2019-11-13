# -*- coding: utf-8 -*-
"""
Unit tests for DecayType.
"""
from __future__ import unicode_literals
from __future__ import print_function

import logging
import os
import shutil
import tempfile
from unittest import TestCase, SkipTest
from unittest.mock import MagicMock

from decay.kind import DecayType

LOGGER = logging.getLogger('tests.decay.host')


class TestDecayType(TestCase):
    def setUp(self):
        self.testee = DecayType('test')

    def tearDown(self):
        self.testee = None

    def test_init(self):
        self.testee = DecayType('test')
        self.assertEqual(self.testee.decay_name, 'test')

    def test_str(self):
        with self.assertRaises(NotImplementedError):
            _ = '%s' % self.testee

    def test_repr(self):
        with self.assertRaises(NotImplementedError):
            _ = '%r' % self.testee

    def test_update_decay(self):
        with self.assertRaises(NotImplementedError):
            _ = '%r' % self.testee.update_decay(1, 2, 3)
