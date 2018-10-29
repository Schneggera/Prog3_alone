""" Unittests fuer den werteTabellenGenerator """

from my_package.generatoren import werte_tabellen_generator

import unittest


class TestWerteTabellenGenerator(unittest.TestCase):
    """ TestCase """
    def setUp(self):
        self.__werte_tabellen_generator = \
            werte_tabellen_generator(0, 1, 5, '+')

    def test_additions_sequenz(self):
        """ Test fuereine Tabelle mit den Operator '+' """
        self.assertEqual(list(self.__werte_tabellen_generator),
                         [1, 2, 3, 4, 5])
