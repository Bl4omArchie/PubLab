from pubcrypt.cryptosystem.rsa import *
from pubcrypt.number.primality import *
from pubcrypt.number.util import *



def launch_test():
    """ Launch this script to see if everything in pubcrypt module is working """
    try:
        n, e, d = generate(2048, e=65537)
        prime_recovery(n, e, d)

        obj = GeneratePrimeNumber(1024, 65537)
        obj.get_prime_factor()

    except:
        ValueError("Test failed")



def generate_rsa_key_pair(nBits):
    n, e, d = generate(nBits)
    return (n, e), (n, d)

def retrieve_prime_factors(n, e, d):
    p, q = prime_recovery(n, e, d)
    return p, q
    

if __name__ == "__main__":
    launch_test()