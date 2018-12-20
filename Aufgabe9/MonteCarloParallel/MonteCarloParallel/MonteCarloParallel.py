import random
import multiprocessing


def monte_carlo(run):
    '''berechnet Pi'''
    hits = i = 0
    while i < run:
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1:
            hits += 1
        i += 1
    return(hits)


if __name__ == '__main__':
    nrOfCores = multiprocessing.cpu_count()
    runs = [10000, 10000, 10000, 10000]
    process_pool = multiprocessing.Pool(processes = nrOfCores)
    l2 = process_pool.map(monte_carlo, runs)
    print(4*sum(l2)/sum(runs))