from pubcrypt.cryptosystem.rsa import *
from pubcrypt.number.primality import *
from pubcrypt.number.util import *
from matplotlib import pyplot as plt
import time


def evaluation(nb):
    x = []  #plot 1
    y = []  #plot 1

    fig, ax = plt.subplots(1, figsize=(15, 10))
    fig.suptitle('KeyPair generation', fontsize=15)

    for _ in range(1, nb+1):
        start_time = time.time()
        generate(2048)
        x.append(_)
        y.append(time.time() - start_time)


    plt.plot(x, y, color="purple", label="generate()")
    plt.legend(loc="upper right", title="Legend", frameon=False)
    plt.show()


def launch_test():
    """ Launch this script to see if everything in pubcrypt module is working """
    try:
        n, e, d = generate(2048, e=65537)
        prime_recovery(n, e, d)
        get_prime_factor(1024, 65537)

    except:
        ValueError("Test failed")

    

if __name__ == "__main__":
    launch_test()
    #evaluation(10)