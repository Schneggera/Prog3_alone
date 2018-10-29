# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

cities = ["A", "B", "C", "D"]
cord = [(100, 50), (30, 60), (70, 20), (10, 10)]
startCity = cities[0]
permutation = []
curPer = [startCity]
citiesTemp = []


def permutations(citiesPer, curPer):
    if len(citiesPer) == 0:        
        curPer.append(startCity)
        return
    
    for cities in citiesPer:
        safePer = curPer.copy()
        citiesTemp = citiesPer.copy()        
        curPer.append(cities)        
        citiesTemp.remove(cities)
        permutations(citiesTemp, curPer)               
        permutation.append(curPer)
        curPer = safePer
        
                

def salesman(permutations)
    for per in permutations
		for perm in per
			x = perm.x - per[perm.index +1]
			y = perm.y - per[perm.index +1]
			length += sqrt(x^2 + y^2)
			
		if length < lengthGes
			lengthGes = length
			
	return lengthGes

				
cities.remove("A")
permutations(cities, curPer)
print(permutation)
