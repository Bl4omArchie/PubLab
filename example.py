from pubcrypt.number.primality import *
from pubcrypt.number.util import *
from pubcrypt.modules.rsa import *
import time


def benchmark():
    #we compare the speed of two function by repeating the function 1000 times
    start_time = time.time()
    for i in range(1, 1000):
        #put your function1 here
        pass

    interval = time.time() - start_time
    print ('Total time in seconds:', interval)


    start_time = time.time()
    for i in range(1, 1000):
        #put your function2 here
        pass

    interval = time.time() - start_time
    print ('Total time in seconds:', interval)


def generate_rsa_key_pair(nBits):
    n, e, d = generate(nBits)
    return (n, e), (n, d)

def retrieve_prime_factors(n, e, d):
    p, q = prime_recovery(n, e, d)
    return p, q

if __name__ == "__main__":
    generate_rsa_key_pair(2048)