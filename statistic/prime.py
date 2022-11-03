from pubcrypt.number.primality import GeneratePrimeNumber
import matplotlib.pyplot as plt
import time

def prime_generation_evaluation(nb):
    x = []  #plot 1
    y = []  #plot 1

    z = []  #plot 2
    w = []  #plot 2


    fig, ax = plt.subplots(1, figsize=(15, 10))
    fig.suptitle('Prime number generation', fontsize=15)

    obj = GeneratePrimeNumber(1024, 65537)
    for _ in range(1, nb+1):
        start_time = time.time()
        
        obj.get_prime_factor()
        y.append(time.time() - start_time)
        print ("p generated")

        x.append(_)
        z.append(_)
        print ("first key finished")

    plt.plot(x, y, color="purple", label="normal prime")
    plt.plot(z, w, color="green", label="asynchrone prime")


    #title and legend of the graph
    plt.legend(loc="upper right", title="Legend", frameon=False)
    plt.show()