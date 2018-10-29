"""
Modul generatoren.
"""

from my_package.manipulatoren import ZahlenManipulator


def werte_tabellen_generator(anfangs_wert, argument, schritt_zahl, operation):
    """
    Erzeugung einer Wertetabelle

    Args:
        anfangs_wert: Untergrenze
        argument: Argument, das wiederholt auf den Wert angewendet wird
        schritt_zahl: Anzahl der Rechenschritte
        operation: Operation, die ausgefuehrt wird, '+', '-', '*', '/'

    Returns:
        Generator fuer die Ergebnis-Werte
    """
    z_m = ZahlenManipulator(anfangs_wert)
    operatoren_verzeichnis = {
        '+': z_m.addieren,
        '*': z_m.multiplizieren,
        '/': z_m.dividieren
        }
    if operation not in operatoren_verzeichnis:
        print("Fehler: illegale Operation", operation)
    else:
        methode = operatoren_verzeichnis[operation]
        for _ in range(schritt_zahl):
            methode(argument)
            yield z_m.get_wert()
