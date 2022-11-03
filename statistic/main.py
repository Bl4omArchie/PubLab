import matplotlib.pyplot as plt
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


def normal_plot(nb):
    x = []  #1 curve
    y = []  #1 curve

    fig, ax = plt.subplots(1, figsize=(25, 15))
    fig.suptitle('Square and multiply speed comparison', fontsize=15)

    for _ in range(1, nb+1):

        start_time = time.time()
        #your function
        y.append(time.time() - start_time)

        x.append(_)

    plt.plot(x, y, color="green")
    plt.legend(loc="upper right", title="Legend", frameon=False)
    plt.show()


def motion_plot(nb):
    x = []
    y = []

    fig, ax = plt.subplots(1, figsize=(25, 15))
    fig.suptitle('Square and multiply speed comparison', fontsize=15)

    for _ in range(1, nb+1):
        start_time = time.time()
        #your function
        y.append(time.time() - start_time)

        x.append(_)
        plt.pause(0.05) # pause avec duree en secondes
        plt.plot(x, y, color="green")


    #title and legend of the graph
    plt.legend(loc="upper right", title="Legend", frameon=False)
    plt.show()