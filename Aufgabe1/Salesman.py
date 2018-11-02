# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
CORD = {"A": (100, 50), "B": (30, 60), "C": (70, 20), "D": (10, 10)}
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
    else:
        cur_per.append(cities_per[-1])
        cur_per.append(STARTCITY)
        lista = ['A']+cur_per
        PERMUTATION.append(lista)
        return


def calc_shortest():
    '''berechnet den kuerzesten weg unter allen Permutationen'''
    cur_dist = 0
    dist = 9999999999
    for per in PERMUTATION:
        for city in per:
            if per.index(city) == len(per):
                continue
            else:
                cur_dist += calc_dist(city, per[per.index(city) + 1])
        if cur_dist < dist:
            dist = cur_dist
    return dist


def calc_dist(city, next_city) -> int:
    '''berchnet den kuerzsten Weg zwischen zwei Punkten'''
    return math.sqrt(((CORD[city][0]-CORD[next_city][0]) *
                      (CORD[city][0]-CORD[next_city][0])) +
                     ((CORD[city][1]-CORD[next_city][1]) *
                      (CORD[city][1]-CORD[next_city][1])))


CITIES = list(CORD.keys())
STARTCITY = CITIES[0]
CITIES.remove(STARTCITY)
permutations(CITIES, cur_per=[])
print(calc_shortest())
