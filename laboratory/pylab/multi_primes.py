from pubcrypt.number.primality import get_prime_factor
from multiprocessing import Queue
import multiprocessing as mp
import time



def launch_test(nb):
    qs = [Queue() for _ in range(nb)]
    procs = []
    result = []

    start_time = time.time()
    ctx = mp.get_context("fork")


    for i in range(nb):
        start_time = time.time()
        proc = ctx.Process(target=get_prime_factor, args=(1024, 65537, qs[i]))
        procs.append(proc)
        proc.start()

    for i in range(nb):
        proc.join()
        result.append(qs[i].get())
    
    print (f"Done in {time.time() - start_time}")
    print ("=========================\n")
    print (f"First key: {result[0] * result[1]}")
    print (f"Second key: {result[2] * result[3]}")
    print (f"Third key: {result[4] * result[5]}")
    print (f"Fouth key: {result[6] * result[7]}")
    print (f"Fifth key: {result[8] * result[9]}")


if __name__ == "__main__":
    mp.set_start_method("fork")
    launch_test(10)