from pubcrypt.rsa import generate
from pubcrypt.number.primality import GeneratePrimeNumber
import matplotlib.pyplot as plt
import time

#--- evaluate keypair generation ---
"""
How to evaluare the efficiency of a key-pair generator ?

1) First we have some simple test about the given bit key size and the public exponent e
2) Then we generate a random prime number twice (p and q)
    | 1) we check if the number is odd and if the number is co-prime with the public exponent
    | 2) we make the miller-rabin test
    | 3) we repeat the operation many time as we need

3) we compute d, phi and the public key N
4) pair wise consistency test



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


def prime_number_evaluation(n, nBits):
    x = []
    y = []
    pBits = nBits//2

    obj = GeneratePrimeNumber(1024, 65537)

    for z in range(1, n+1):
        p, i = obj.get_prime_factor(pBits, 65537)
        y.append(i)
        x.append(z)

    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    prime_number_evaluation(10, 2048)