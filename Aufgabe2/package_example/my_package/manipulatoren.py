"""
Modul manipulatoren.
"""

from __future__ import division


class ZahlenManipulator(object):
    """
    Klasse zur Manipulation einer Zahl.
    """

    def __init__(self, w=None):
        """
        Konstruktur

        Args:
            w: Initialer Wert der Zahl
        """
        self.__wert = w

    def get_wert(self):
        """
        Auslesen des aktuellen Werts.

        Returns:
            Wert der Zahl.
        """
        return self.__wert

    def set_wert(self, wert):
        """ Setzen des Werts auf wert. """
        self.__wert = wert

    def addieren(self, delta):
        """ Erhoehen des Wertes um delta """
        self.__wert += delta

    def subtrahieren(self, delta):
        """ Vermindern des Wertes um delta """
        self.__wert -= delta

    def dividieren(self, div):
        """ Division des Wertes durch div """
        self.__wert /= div

    def multiplizieren(self, faktor):
        """ Multiplikation des Wertes mit faktor """
        self.__wert *= faktor
