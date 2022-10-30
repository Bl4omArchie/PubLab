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