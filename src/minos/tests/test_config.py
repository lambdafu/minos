from StringIO import StringIO

import unittest

from minos import Config
import minos.config

class TestConfig(unittest.TestCase):
    def test_empty(self):
        cfg = Config.fromstring("")
        self.assertEqual(cfg, minos.config.DEFAULT)

    def test_simple(self):
        address = "bolt://neo4j.example.com/"
        input = StringIO('''
        [neo4j]
        address = "%s"
        ''' % address)
        cfg = Config.parse(input)
        self.assertEqual(cfg.neo4j.address, address)
