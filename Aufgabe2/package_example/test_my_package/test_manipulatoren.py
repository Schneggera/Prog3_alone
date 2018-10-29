""" Testmodul fuer die Klasse Zahlenmanipulator"""

from my_package.manipulatoren import ZahlenManipulator
import unittest


class TestZahlenManipulator(unittest.TestCase):
    """ TestCase fuer den ZahlenManipulator"""

    def setUp(self):
        self.__zahlen_manipulator = ZahlenManipulator()

    def test_addieren(self):
        """ Test der Addier-Methode"""
        self.__zahlen_manipulator.set_wert(38)
        self.__zahlen_manipulator.addieren(4)
        self.assertEqual(self.__zahlen_manipulator.get_wert(), 42)

    def test_division_multiplikation(self):
        """ Test der Divisions-Methode """
        self.__zahlen_manipulator.set_wert(1)
        self.__zahlen_manipulator.dividieren(3)
        self.__zahlen_manipulator.multiplizieren(3)
        self.assertEqual(self.__zahlen_manipulator.get_wert(), 1)
