'''importiert Randomfunktion'''
import random
import multiprocessing
import math


def monte_carlo(qIN, qOUT):
    '''berechnet Pi'''
    while True:
        hits = i = 0
        while i < qIN.get():
            x = random.random()
            y = random.random()
            if x*x + y*y <= 1:
                hits += 1
            i += 1
            qOUT.put(hits)
            qIN.task_done()


if __name__ == '__main__':
    argumentQueue = multiprocessing.JoinableQueue()
    resultQueue = multiprocessing.Queue()
    nrOfProcesses = multiprocessing.cpu_count()
    processes = [multiprocessing.Process(
                            target = monte_carlo,
                            args = (argumentQueue, resultQueue))
                    for i in range(nrOfProcesses)]
    for i in range(0, 5):
        argumentQueue.put(i)
    for p in processes:
        p.start()
    for p in processes:
        p.terminate()
    for i in range(10):
        print(resultQueue.get(), end=' ')

