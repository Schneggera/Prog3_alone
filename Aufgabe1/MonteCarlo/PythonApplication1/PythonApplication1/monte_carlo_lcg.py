import time

def monte_carlo():
    '''berechnet Pi'''
    hits = i = 0
    run = 10000000
    while i < run:
        x = next(lcg(2**32, 22695477, 1))    #c values
        y = next(lcg(2**48, 25214903917 , 11))    #java values
        if x*x + y*y <= 1:
            hits += 1
        i += 1
    print(4*hits/run)

def lcg(modulus, a, c, seed = time.time()*1000):
    while True:
        seed = (a * seed + c) % modulus
        yield seed

monte_carlo()
