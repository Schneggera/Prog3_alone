# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
from PyQt5 import QtWidgets
import random as ran


def roll_dice():
    w.tb1.setText(u"\u25CB")
    w.tb2.setText(u"\u25CB")
    w.tb3.setText(u"\u25CB")
    w.tb4.setText(u"\u25CB")
    w.tb5.setText(u"\u25CB")
    w.tb6.setText(u"\u25CB")
    num = ran.randint(1, 6)
    if num > 5:
        w.tb6.setText(u"\u25CF")
    if num > 4:
        w.tb5.setText(u"\u25CF")
    if num > 3:
        w.tb4.setText(u"\u25CF")
    if num > 2:
        w.tb3.setText(u"\u25CF")
    if num > 1:
        w.tb2.setText(u"\u25CF")
    w.tb1.setText(u"\u25CF")







app = QtWidgets.QApplication(sys.argv)
w = loadUi("/home/pyoneer/Schreibtisch/test/mainwindow.ui")

w.roll_Dices.clicked.connect(roll_dice)

w.show()
sys.exit(app.exec_())
