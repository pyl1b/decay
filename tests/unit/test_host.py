# -*- coding: utf-8 -*-
"""
Unit tests for Host.
"""
from __future__ import unicode_literals
from __future__ import print_function

import logging
import os
import shutil
import tempfile
from unittest import TestCase, SkipTest
from unittest.mock import MagicMock

from decay.host import Host

LOGGER = logging.getLogger('tests.decay.host')


class TestTestee(TestCase):
    def setUp(self):
        self.testee = Host()

    def tearDown(self):
        self.testee = None

    def test_init(self):
        self.testee = Host()
