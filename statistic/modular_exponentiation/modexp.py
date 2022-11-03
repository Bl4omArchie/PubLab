from pubcrypt.number.util import int_to_bin
from multiprocessing import Process


def mod_exp(base, exp, mod):
    return base**exp % mod


def memory_efficient(base, exp, mod):
    c = 1
    for _ in range(0, exp-1):
        c = (c*base) % mod
    return c


def binary_shift(base, exp, mod):
    result = 1
    base = base % mod

    while exp > 0:
        if exp % 2 == 1:
            result = (result*base) % mod
        exp = exp >> 1
        base = (base*base) % mod
    return result


def square_multiply(x, h, n):
    t = int_to_bin(h)
    r = x

    for i in range(len(t)-1):
        r = (r**2) % n
        if t[i] == "1":
            r = (r*x) % n
    return r


#winner
def pow_mod(x, y, z=0):
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number


def launch_mod_exp(base, exp, mod):
    proc1 = Process(target=mod_exp, args=(base, exp, mod))
    proc1.start()

def launch_memory_efficient(base, exp, mod):
    proc2 = Process(target=memory_efficient, args=(base, exp, mod))
    proc2.start()

def launch_binary_shift(base, exp, mod):
    proc3 = Process(target=binary_shift, args=(base, exp, mod))
    proc3.start()

def launch_square_multiply(base, exp, mod):
    proc4 = Process(target=square_multiply, args=(base, exp, mod))
    proc4.start()

def launch_pow_mod(base, exp, mod):
    proc5 = Process(target=pow_mod, args=(base, exp, mod))
    proc5.start()