from pubcrypt.number.util import int_to_bin
from laboratory.publab.modular_exponentiation.modexp import *

import matplotlib.pyplot as plt
from random import randrange
import time


def square_multiply_evaluation(nb, case):
    x = []  #plot 1
    y = []  #plot 1

    z = []  #plot 2
    w = []  #plot 2

    u = []  #plot 3
    v = []  #plot 3

    i = []  #plot 4
    j = []  #plot 4

    t = []  #plot 5
    r = []  #plot 5

    t1 = []  #plot 5
    r1 = []  #plot 5

    fig, ax = plt.subplots(1, figsize=(15, 10))
    fig.suptitle('Square and multiply speed comparison', fontsize=15)

    for _ in range(1, nb+1):
        if case == 1:
            c = randrange(1, 1000)
            e = 3
            n = randrange(2**16, 2**17-1)
        elif case == 2:
            c = randrange(1000, 5000)
            e = 513
            n = randrange(2**64, 2**65-1)
        else:
            c = randrange(10000, 50000)
            e = 65537
            n = randrange(2**512, 2**513-1)


        start_time = time.time()
        """
        mod_exp(c, e, n)
        y.append(time.time() - start_time)

        start_time = time.time()
        memory_efficient(c, e, n)
        w.append(time.time() - start_time)

        start_time = time.time()
        binary_shift(c, e, n)
        v.append(time.time() - start_time)

        start_time = time.time()
        square_multiply(c, e, n)
        j.append(time.time() - start_time)
        """

        start_time = time.time()
        pow_mod(c, e, n)
        r.append(time.time() - start_time)

        start_time = time.time()
        pow(c, e, n)
        r1.append(time.time() - start_time)



        #x.append(_)
        #z.append(_)
        #u.append(_)
        #i.append(_)
        t.append(_)
        t1.append(_)

    """
    plt.plot(x, y, color="green", label="mod_exp()")
    plt.plot(z, w, color="blue", label="memory_efficient()")
    plt.plot(u, v, color="red", label="binary_shift()")
    plt.plot(i, j, color="yellow", label="square_multiply()")
    """
    plt.plot(t, r, color="purple", label="pow_mod()")
    plt.plot(t1, r1, color="green", label="launch_pow_mod()")


    #title and legend of the graph
    plt.legend(loc="upper right", title="Legend", frameon=False)
    plt.show()