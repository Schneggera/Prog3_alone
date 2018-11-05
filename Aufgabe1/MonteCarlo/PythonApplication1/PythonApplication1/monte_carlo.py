'''importiert Randomfunktion'''
import random


def monte_carlo():
    '''berechnet Pi'''
    hits = i = 0
    run = 10000000
    while i < run:
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1:
            hits += 1
        i += 1
    print(4*hits/run)


monte_carlo()
