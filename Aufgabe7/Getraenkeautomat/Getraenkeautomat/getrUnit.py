
class getr():
    COINS = ['50Cent', '1Cent', '2Cent', '5Cent','10Cent', '20Cent', '1Euro', '2Euro', 'beenden']
    DRINKS = ['Limonade', 'Mineralwasser', 'beenden']

    def __init__(self):
        self.zustand = "Anfang"
        self.used = False

    def eingabe(self, inp):
        if inp in self.COINS and self.zustand == "Anfang":
            self.zustand = "Auswahl"
            if self.used == True:
                print("Ausgabe: Bitte waehlen")
            else:
                return "Ausgabe: Bitte waehlen"            
        elif inp in self.DRINKS and self.zustand == "Auswahl":
            self.zustand = "Anfang"
            if self.used == True:
                print("Ausgabe: Bitte " + inp + " entnehmen!")
            else:
                return "Ausgabe: Bitte " + inp + " entnehmen!"
        else:
            self.zustand = "falscheMünze"
            if self.used == True:
                print("Ausgabe: eingabeSpeichern")
            else:
                return "Ausgabe: eingabeSpeichern"

    def zustandsAusgabe(self):
        if self.zustand == "Anfang":
            if self.used == True:
                print("Zustand: \t" + self.zustand + '\n' +
                      "Befehle: \t" + ('[%s]' % ', '.join(map(str, self.COINS))))
            else:
                return ("Zustand: " + self.zustand +
                        " Befehle: " + ('[%s]' % ', '.join(map(str, self.COINS))))
        elif self.zustand == ("Auswahl" or "falscheMünze"):
            if self.used == True:
                print("Zustand: \t" + self.zustand + '\n' + 
                      "Befehle: \t" + ('[%s]' % ', '.join(map(str, self.DRINKS))))
            else:
                return ("Zustand: " + self.zustand + 
                        " Befehle: " + ('[%s]' % ', '.join(map(str, self.DRINKS))))

    def change_use(self):
        if self.used == False:
            self.used = True
        elif self.used == True:
            self.used = False



import unittest
class getrTest(unittest.TestCase):
    def setUp(self):
        from Getraenkeautomat import getr
        self.g = getr()

    def test_eingabe(self):
        self.g.zustandsAusgabe()
        self.assertEqual(self.g.zustandsAusgabe(), 'Zustand: Anfang Befehle: [50Cent, 1Cent, 2Cent, 5Cent, 10Cent, 20Cent, 1Euro, 2Euro, beenden]')
        self.assertEqual(self.g.eingabe('50Cent'), 'Ausgabe: Bitte waehlen')
        self.assertEqual(self.g.zustandsAusgabe(), 'Zustand: Auswahl Befehle: [Limonade, Mineralwasser, beenden]')
