from pubcrypt.number.util import square_multiply

import matplotlib.pyplot as plt
from random import randrange
import time


def square_multiply_evaluation(nb):
    x = []
    y = []
    z = []
    w = []

    fig, ax = plt.subplots(1, figsize=(15, 10))
    fig.suptitle('Square and multiply speed comparison', fontsize=15)

    for _ in range(1, nb+1):
        c = randrange(1, 100)
        e = randrange(1, 25)
        n = randrange(1, 100000)

        start_time = time.time()
        pow(c, e, n)
        y.append(time.time() - start_time)

        start_time = time.time()
        square_multiply(c, e, n)
        w.append(time.time() - start_time)

        x.append(_)
        z.append(_)
    plt.plot(x, y, color="green", label="pow()")
    plt.plot(z, w, color="blue", label="square_multiply()")


    #title and legend of the graph
    plt.legend(loc="upper right", title="Legend", frameon=False)
    plt.show()