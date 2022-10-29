from pubcrypt.rsa import generate
from pubcrypt.number.primality import GeneratePrimeNumber
import matplotlib.pyplot as plt
import time

#--- evaluate keypair generation ---
"""
How to evaluare the efficiency of a key-pair generator ?

1) we check if the number is odd and if the number is co-prime with the public exponent
2) we make the miller-rabin test
3) we repeat the operation many time as we need

"""

def generation_time(n, nBits):
    x = []
    y = []

    for i in range(1, n+1):
        start_time = time.time()
        generate(nBits)
        y.append(time.time() - start_time)
        x.append(i)

    plt.plot(x, y)
    plt.show()


def prime_number_evaluation(n, pBits):
    x = []
    y = []

    obj = GeneratePrimeNumber(pBits, 65537)

    for z in range(1, n+1):
        obj.get_prime_factor()
        y.append(obj.i)
        x.append(z)

    plt.plot(x, y)
    plt.show()


def prime_number_evaluation_with_time(n, pBits):
    x = []
    y = []

    obj = GeneratePrimeNumber(pBits, 65537)

    for _ in range(1, n+1):
        start_time = time.time()
        obj.get_prime_factor()
        y.append(time.time() - start_time)
        x.append(obj.i)

    plt.plot(x, y)
    plt.show()