# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
cities = ["A", "B", "C", "D"]
cord = [(100, 50), (30, 60), (70, 20), (10, 10)]
startCity = cities[0]
permutation = []


def permutations(citiesPer, curPer):
    if len(citiesPer) > 1:
        for city in citiesPer:
           curPer.append(city)
           citiesTemp = list(citiesPer)
           citiesTemp.remove(city)
           perhigher = curPer[:]
           permutations(citiesTemp, curPer)
           curPer = perhigher[:-1]           
        return
    else:
        curPer.append(citiesPer[-1])
        curPer.append(startCity)
        lista = ['A']+curPer
        permutation.append(lista)
        return

def calc_shortest():
    for per in permutation:
        for city in permutation:





cities.remove(startCity)
permutations(cities, curPer=[])
print(permutation)
