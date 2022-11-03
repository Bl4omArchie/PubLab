from time import perf_counter, sleep
from contextlib import contextmanager
from random import randint
from multiprocessing import Process

Npr = 2

@contextmanager
def timing(message):
    to = perf_counter()
    yield
    print ("*chrono > ", message, perf_counter()-to)


def primeFactors(n):
    primfac = []
    d = 2

    while d*d <= n:
        while not (n%d):
            primfac.append(d)
            n //= d
        d += 1

    if n>1: primfac.append(n)
    return primfac

def execProc():
    for _ in range(30000//Npr):
        r = randint(20000, 100000000)
        pf = primeFactors(r)
        print (f"Facteur de r: {pf}")


def main():
    with timing(f"Facteurs multi (Npr): "):
        procs = []
        for _ in range(Npr):
            proc = Process(target=execProc, args=())
            procs.append(proc)
            proc.start()

        for proc in procs:
            proc.join()

if __name__ == "__main__":
    main()