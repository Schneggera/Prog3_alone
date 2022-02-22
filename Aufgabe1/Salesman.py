# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

'''
"A": (0.010319427306382911, 0.8956251389386756), "B": (0.6999898714299346, 0.42254500074835377),
"C": (0.4294574582950912, 0.4568408794115657), "D": (0.6005454852683483, 0.9295407203370832),
"E": (0.9590226056623925, 0.581453646599427), "F": (0.748521134122647, 0.5437775417153159),
"G": (0.7571232013282426, 0.606435031856663), "H": (0.07528757443413125, 0.07854082131763074),
"I": (0.32346175150639334, 0.7291706487873425)
'''

CORD = {"A": (0.010319427306382911, 0.8956251389386756), "B": (0.6999898714299346, 0.42254500074835377),
        "C": (0.4294574582950912, 0.4568408794115657), "D": (0.6005454852683483, 0.9295407203370832),
        "E": (0.9590226056623925, 0.581453646599427), "F": (0.748521134122647, 0.5437775417153159),
        "G": (0.7571232013282426, 0.606435031856663)}
PERMUTATION = []


def permutations(cities_per, cur_per):
    '''ermittelt alle Permutationen'''
    if len(cities_per) > 1:
        for city in cities_per:
            cur_per.append(city)
            cities_temp = list(cities_per)
            cities_temp.remove(city)
            perhigher = cur_per[:]
            permutations(cities_temp, cur_per)
            cur_per = perhigher[:-1]
        return
    else:
        cur_per.append(cities_per[-1])
        cur_per.append(STARTCITY)
        lista = ['A']+cur_per
        PERMUTATION.append(lista)
        return


def calc_shortest():
    '''berechnet den kuerzesten weg unter allen Permutationen'''
    dist = float.inf
    for per in PERMUTATION:
        cur_dist = 0
        for city in range(len(per) -1):
                cur_dist += calc_dist(per[city], per[city + 1])
        if cur_dist < dist:
            shortest_per = per
            dist = cur_dist
    return dist, shortest_per


def calc_dist(city, next_city) -> int:
    '''berechnet den kuerzsten Weg zwischen zwei Punkten'''
    return math.sqrt(((CORD[city][0]-CORD[next_city][0]) *
                      (CORD[city][0]-CORD[next_city][0])) +
                     ((CORD[city][1]-CORD[next_city][1]) *
                      (CORD[city][1]-CORD[next_city][1])))

def pfad_ausgabe(path):
    pointArray = np.array(path)
    plt.plot(pointArray[0,0], pointArray[0,1], 'ro')
    plt.plot(pointArray[1:-1,0], pointArray[1:-1,1], 'bo')
    plt.plot(pointArray[:,0], pointArray[:,1], '-k')
    plt.yticks(())
    plt.xticks(())
    plt.show()

def shortest_to_list(shortest):
    a = []
    for city in shortest:
        a.append(CORD.get(city))
    return a

CITIES = list(CORD.keys())
STARTCITY = CITIES[0]
CITIES.remove(STARTCITY)
permutations(CITIES, cur_per=[])
pfad_ausgabe(shortest_to_list(calc_shortest()[1]))
print(calc_shortest())
