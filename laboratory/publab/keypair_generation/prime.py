from pubcrypt.number.primality import GeneratePrimeNumber
from pubcrypt.number.util import pow_exp, pow_mod, gcd, isqrt, RNG
from multiprocessing import Process, Queue
from random import randrange
import matplotlib.pyplot as plt
import time



def launch_process(pBits, e): 
    qs = [Queue() for _ in range(2)]


    proc1 = Process(target=get_prime_factor, args=(pBits, e, qs[0]))
    proc2 = Process(target=get_prime_factor, args=(pBits, e, qs[1]))
    proc1.start()
    proc2.start()


    primes = []
    while qs[0].get() == 0:
        primes.append(qs[0].get())
    proc1.join()
    print (primes)

    while qs[1].get() == 0:
        primes.append(qs[1].get())
    proc2.join()

    print (primes)
    return primes[0], primes[1]



def get_prime_factor(pBits, e, qout):
    candidate = 0

    while candidate == 0:
        p = RNG(pBits)
        if p%2 == 0:
            p += 1

        if p >= isqrt(2)*(pow_exp(2, pBits-1)):
            if gcd(p-1, e) == 1:
                candidate = miller_rabin(p, 5)
    qout.put(p)


def miller_rabin(p, r):
    """Credit: https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python"""
    s = 0
    d = p-1
    while d%2==0:
        d>>=1
        s+=1
    assert(pow_exp(2, s) * d == p-1)
    
    def trial_composite(a):
        if pow_mod(a, d, p) == 1:
            return 0

        for i in range(s):
            if pow_mod(a, pow_exp(2, i) * d, p) == p-1:
                return 0
            return 1 
        
    for _ in range(r): #number of trials 
        a = randrange(2, p)
        if trial_composite(a):
            return 0
    return 1



def prime_generation_evaluation(nb):
    x = []  #plot 1
    y = []  #plot 1

    z = []  #plot 2
    w = []  #plot 2


    fig, ax = plt.subplots(1, figsize=(15, 10))
    fig.suptitle('Prime number generation', fontsize=15)

    obj = GeneratePrimeNumber(1024, 65537)
    for _ in range(1, nb+1):
        start_time = time.time()
        
        obj.get_prime_factor()
        y.append(time.time() - start_time)
        print ("p generated")

        x.append(_)
        z.append(_)
        print ("first key finished")

    plt.plot(x, y, color="purple", label="normal prime")
    plt.plot(z, w, color="green", label="asynchrone prime")


    #title and legend of the graph
    plt.legend(loc="upper right", title="Legend", frameon=False)
    plt.show()