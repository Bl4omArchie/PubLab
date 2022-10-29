from pubcrypt.number.util import *


def get_prime_factor(pBits, e):
    candidate = 0
    i = 0
    while candidate == 0:
        p = RNG(pBits)
        if p%2 == 0:
            p += 1

        if p >= isqrt(2)*(pow(2, pBits-1)):
            if gcd(p-1, e) == 1:
                candidate = miller_rabin(p, pBits, 5)
        i += 1

    return p, i


def miller_rabin(w, wLen, r):
    """Credit: https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python"""
    s = 0
    d = w-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == w-1)
 
    def trial_composite(a):
        if pow(a, d, w) == 1:
            return 0

        for i in range(s):
            if pow(a, 2**i * d, w) == w-1:
                return 0
        return 1  
 
    for i in range(r): #number of trials 
        a = randrange(2, w)
        if trial_composite(a):
            return 0
    return 1