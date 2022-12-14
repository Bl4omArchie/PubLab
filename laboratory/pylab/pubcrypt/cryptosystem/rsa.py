from pubcrypt.number.primality import get_prime_factor
from multiprocessing import Process, Queue
from pubcrypt.number.util import *
from random import randrange


def generate(nBits, e=65537):
    if nBits < 2048:
        raise ValueError(("Incorrect key length. nBits must be equal or greater than 2048"))
    
    elif e%2 == 0 or not pow_exp(2, 16) <= e <= pow_exp(2, 256):
        raise ValueError("Incorrect puclic exponent. e must be odd and in the range [2^16, 2^256]")

    pBits = nBits//2
    primes = [Queue(), Queue()]

    proc1 = Process(target=get_prime_factor, args=(pBits, e, primes[0]))
    proc2 = Process(target=get_prime_factor, args=(pBits, e, primes[1]))
    proc1.start() ; proc2.start()

    proc1.join() ; p = primes[0].get()
    proc2.join() ; q = primes[1].get()
    
    d = invmod(e, lcm(p-1, q-1))
    n = p * q

    if pair_wise_consistency_test(n, e, d) == 0:
        raise ValueError("Error, please retry. Consistency test failed")

    return n, e, d


def primitive_exp(m, exp, n):
    """ This function represent the encryption/decryption/signature operation """
    if 0 < m < n-1:
        return pow_mod(m, exp, n)

    else:
        raise ValueError("Data representative out of range")


def prime_recovery(n, e, d):
    a = (d*e-1) * gcd(n-1, d*e-1)
    m = a//n
    r = a - m*n
    b = (n-r) // (m+1) +1

    if pow_exp(b, 2) <= 4*n:
        raise ValueError("Error")

    y = isqrt(pow_exp(b, 2)-4*n)
    return (b+y) // 2, (b-y) // 2


def pair_wise_consistency_test(n, e, d):
    m = randrange(1, n//2)
    return m == primitive_exp(m, e*d, n)