from pubcrypt.cryptosystem.rsa import generate 
import time




if __name__ == "__main__":
    start_time = time.time()
    generate(2048)
    print (f"Done in {time.time() - start_time}")