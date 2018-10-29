"""
Modul verdopplung.
"""
# -*- coding: utf-8 -*-


def verdopplungs_funktion(zahl):
    """
    Diese Funktion gibt das mit zwei multiplizierte Argument zurueck

    Args:
        zahl: Referenz auf das zu verdoppelnde Objekt

    Returns:
        2 * zahl

    Examples:
        >>> import math
        >>> [ verdopplungs_funktion(i) for i in [1, 2, 'na'] ]
        [2, 4, 'nana']
        >>> verdopplungs_funktion(math.sin) #doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        TypeError:
    """
    return 2 * zahl

if __name__ == "__main__":
    verdopplungs_funktion
    import doctest
    doctest.testmod()
