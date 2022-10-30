from statistic.modular_exp import square_multiply_evaluation
from pubcrypt.number.util import *
from pubcrypt.rsa import *



def generate_rsa_key_pair(nBits):
    n, e, d = generate(nBits)
    return (n, e), (n, d)

def retrieve_prime_factors(n, e, d):
    p, q = prime_recovery(n, e, d)
    return p, q
    

if __name__ == "__main__":
    square_multiply_evaluation(500)