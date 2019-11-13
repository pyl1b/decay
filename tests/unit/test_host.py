# -*- coding: utf-8 -*-
"""
Unit tests for DecayHost.
"""
from __future__ import unicode_literals
from __future__ import print_function

import logging
import os
import shutil
import tempfile
from unittest import TestCase, SkipTest
from unittest.mock import MagicMock

from decay.host import DecayHost

LOGGER = logging.getLogger('tests.decay.host')


class TestDecayHost(TestCase):
    def setUp(self):
        self.testee = DecayHost()

    def tearDown(self):
        self.testee = None

    def test_init(self):
        self.testee = DecayHost()
        self.assertIsNone(self.testee.decay_type)
        self.assertIsNone(self.testee.decay_ticks_to_0)

        self.testee = DecayHost('type', 9)
        self.assertEqual(self.testee.decay_type, 'type')
        self.assertEqual(self.testee.decay_ticks_to_0, 9)
