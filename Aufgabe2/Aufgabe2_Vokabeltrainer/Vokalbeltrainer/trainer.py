# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random


class Vokabeltrainer:
    'Variablen der Vokabeltrainerklasse'
    voc_dict = {}
    right, false = 0, 0

    def __init__(self, voc):
        'Initialisierung des Dictionary'
        self.voc_dict = voc

    def hinzufuegen(self, key, value):
        'Fuegt neuen Wert zum Dict hinzu'
        self.voc_dict[key] = value

    def training(self, rounds):
        'Startet ein Training'
        for _ in range(rounds):
            word = random.choice(list(self.voc_dict.keys()))
            print('Was ist das englische Wort fuer:', word)
            _a = input('Wort eingeben:')
            if _a.lower() == self.voc_dict.get(word).lower():
                print('Das ist richtig! \n')
                self.right += 1
            else:
                print('Das ist leider falsch! \n')
                self.false += 1
        self.ergebnis_ausgabe()

    def ergebnis_ausgabe(self):
        'Gibt das Ergebnis aus'
        print('Du hattest ' + str(self.right) +
              ' richtig und ' + str(self.false) +
              ' falsch')

    def zuruecksetzen(self):
        'Setzt das Programm zurueck'
        self.right, self.false = 0, 0


class main:
    vdic = {'Haus': 'house', 'Tuer': 'door', 'Geld': 'Money'}
    trainer = Vokabeltrainer(vdic)
    trainer.hinzufuegen('Wasser', 'water')
    trainer.training(3)
    trainer.ergebnis_ausgabe()
    trainer.zuruecksetzen()
    trainer.ergebnis_ausgabe()
