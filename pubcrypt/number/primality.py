from pubcrypt.number.util import *
from random import randrange


class GeneratePrimeNumber():
    def __init__(self, pBits, e) -> None:
        self.pBits = pBits
        self.e = e

    def get_prime_factor(self):
        candidate = 0

        while candidate == 0:
            self.p = RNG(self.pBits)
            if self.p%2 == 0:
                self.p += 1

            if self.p >= isqrt(2)*(pow_exp(2, self.pBits-1)):
                if gcd(self.p-1, self.e) == 1:
                    candidate = self.miller_rabin(5)

        return self.p


    def miller_rabin(self, r):
        """Credit: https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python"""
        s = 0
        d = self.p-1
        while d%2==0:
            d>>=1
            s+=1
        assert(pow_exp(2, s) * d == self.p-1)
    
        def trial_composite(a):
            if pow_mod(a, d, self.p) == 1:
                return 0

            for i in range(s):
                if pow_mod(a, pow_exp(2, i) * d, self.p) == self.p-1:
                    return 0
            return 1  
    
        for _ in range(r): #number of trials 
            a = randrange(2, self.p)
            if trial_composite(a):
                return 0
        return 1