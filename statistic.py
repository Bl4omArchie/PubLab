from pubcrypt.modules.rsa import generate
from pubcrypt.number.primality import get_prime_factor
import matplotlib.pyplot as plt
import time

#--- evaluate_keypair_generation ---
def generation_time(n, nBits):
    x = []
    y = []

    for i in range(n):
        start_time = time.time()
        generate(nBits)
        y.append(time.time() - start_time)
        x.append(i)

    plt.plot(x, y)
    plt.label("evaluation of the efficiency of the keypair generation function")
    plt.show()


def prime_number_evaluation(n, nBits):
    x = []
    y = []
    pBits = nBits//2

    for z in range(n):
        p, i = get_prime_factor(65537, pBits)
        y.append(i)
        x.append(z)

    plt.plot(x, y)
    plt.show()


prime_number_evaluation(10, 2048)