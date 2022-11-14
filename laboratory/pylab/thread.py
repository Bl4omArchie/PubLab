from matplotlib import pyplot as plt
from multiprocessing import Queue
import multiprocessing as mp
import time

""" Find primes numbers with Multi-threading """


def main_thread():
    x = [100, 500, 1000, 10000]
    y = []  #1 curve
    procs = []
    result = []

    fig, ax = plt.subplots(1, figsize=(10, 5))
    fig.suptitle('Find prime numbers', fontsize=15)
    ctx = mp.get_context("fork")

    qs = [Queue() for _ in range(len(x))]

    t = 0
    for i in x:
        start_time = time.time()
        proc = ctx.Process(target=eratosthene, args=(i, qs[t]))
        procs.append(proc)
        proc.start()
        y.append(time.time() - start_time)
        t += 1

    
    t = 0
    for _ in procs:
        proc.join()
        result.append(qs[t].get())
        t += 1
    
    plt.plot(x, y, color="green")
    plt.show()

    for i in range(len(x)):
        print (f"case {i}: {result[i]}")



def eratosthene(n, qout):
    L = [ i for i in range(2,n+1) ]
    P = [ ]
    
    while len(L) != 0:
        P.append(L[0])
        i = L[0]
        for k in L:
            if k % i == 0:
                del(L[L.index(k)])
    
    qout.put(P)


if __name__ == "__main__":
    mp.set_start_method("fork")
    main_thread()


"""
def both():
    x = [100, 500, 1000, 10000]
    y = []  #1 curve
    z = []  #2 curve
    procs = []

    fig, ax = plt.subplots(1, figsize=(10, 5))
    fig.suptitle('Find prime numbers', fontsize=15)

    for i in x:
        start_time = time.time()
        eratosthene(i)
        z.append(time.time() - start_time)

    plt.plot(x, y, color="green")
    plt.plot(x, z, color="red")
    plt.show()

def main():
    x = [100, 500, 1000, 10000]
    y = []  #1 curve

    fig, ax = plt.subplots(1, figsize=(10, 5))
    fig.suptitle('Find prime numbers', fontsize=15)

    for i in x:

        start_time = time.time()
        eratosthene(i)
        y.append(time.time() - start_time)

    plt.plot(x, y, color="red")
    plt.show()

"""