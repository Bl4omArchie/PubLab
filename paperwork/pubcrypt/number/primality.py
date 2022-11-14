from pubcrypt.number.util import pow_exp, pow_mod, gcd, isqrt, RNG
from random import randrange



def get_prime_factor(pBits, e):
    candidate = 0

    while candidate == 0:
        p = RNG(pBits)
        if p%2 == 0:
            p += 1

        if p >= isqrt(2)*(pow_exp(2, pBits-1)):
            if gcd(p-1, e) == 1:
                candidate = miller_rabin(p, 5)
    return p


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