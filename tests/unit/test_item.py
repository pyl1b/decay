# -*- coding: utf-8 -*-
"""
Unit tests for DecayItem.
"""
from __future__ import unicode_literals
from __future__ import print_function

import logging
import os
import shutil
import tempfile
from unittest import TestCase, SkipTest
from unittest.mock import MagicMock

from decay.item import DecayItem

LOGGER = logging.getLogger('tests.decay.item')


class TestDecayItem(TestCase):
    def setUp(self):
        self.testee = DecayItem()

    def tearDown(self):
        self.testee = None

    def test_init(self):
        self.testee = DecayItem()
        self.assertEqual(self.testee.decay_strength, 1.0)
        self.assertIsNone(self.testee.decay_time)

        self.testee = DecayItem(0.5, 9)
        self.assertEqual(self.testee.decay_strength, 0.5)
        self.assertEqual(self.testee.decay_time, 9)

    def test_str(self):
        self.testee = DecayItem()
        self.assertIn('#Invalid', '%s' % self.testee)
        self.assertIn('None', '%r' % self.testee)
        self.assertIn('1.0', '%r' % self.testee)

        self.testee = DecayItem(0.5, 99)
        self.assertNotIn('#Invalid', '%s' % self.testee)
        self.assertIn('99', '%r' % self.testee)
        self.assertIn('0.5', '%r' % self.testee)

    def test_set_decay(self):

        self.testee.set_decay(new_tick=99, new_strength=0.0)
        self.assertEqual(self.testee.decay_time, 99)
        self.assertEqual(self.testee.decay_strength, 0.0)

        self.testee.set_decay(new_tick=99, new_strength=0.5)
        self.assertEqual(self.testee.decay_time, 99)
        self.assertEqual(self.testee.decay_strength, 0.5)

        self.testee.set_decay(new_tick=99, new_strength=1.5)
        self.assertEqual(self.testee.decay_time, 99)
        self.assertEqual(self.testee.decay_strength, 1.0)

        self.testee.set_decay(new_tick=99, new_strength=-1.5)
        self.assertEqual(self.testee.decay_time, 99)
        self.assertEqual(self.testee.decay_strength, 0.0)
