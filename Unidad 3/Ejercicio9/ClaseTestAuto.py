import unittest

from ClaseAuto import Auto


class TestAuto(unittest.TestCase):
    __auto = None
    def setUp(self):
        self.__auto = Auto('X7')

    def test_esAuto(self):
        self.assertTrue(self.__auto.esAuto())

    def test_noesAuto(self):
        self.assertFalse(self.__auto.esAuto())

    
