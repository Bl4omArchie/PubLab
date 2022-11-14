from multiprocessing import Process, Queue
from matplotlib import pyplot as plt
import numpy as np



def test():
    NN = 300
    qs = [Queue() for _ in range(5)]

    fin = 'FIN'

    xs = np.linspace(0.0, 3.0, NN)
    for x in xs:
        qs[0].put(x)
        qs[2].put(x)
    qs[0].put(fin)
    qs[2].put(fin)

    pex = Process(target=ex, args=(qs[0], qs[1]))
    psi = Process(target=si, args=(qs[2], qs[3]))
    pmul = Process(target=mul, args=(qs[1], qs[3], qs[4]))
    pex.start()
    psi.start()
    pmul.start()
    
    pex.join()
    psi.join()

    ys = []
    while not qs[4].empty(): 
        ys.append(qs[4].get())
    pmul.join()

    print (ys)
    
def ex(qin, qout):
    while True:
        x = qin.get()
        if x == 'FIN':
            qout.put('FIN')
            break
        qout.put(np.exp(-x))

def si(qin, qout):
    while True:
        x = qin.get()
        if x == 'FIN':
            qout.put('FIN')
            break
        qout.put(np.sin(20.0*x))

def mul(qi1, qi2, qout):
    while True:
        x = qi1.get()
        y = qi2.get()

        if x == 'FIN' and y == 'FIN': break
        qout.put(x*y)

if __name__ == "__main__":
    test()