import time
import math

def checkprime_slow(n):
    if n == 1 or n == 2 or n == 3:
        return True
    if n % 2 == 0 :
        return False
    elif n % 3 == 0 :
        return False
    else :
        for i in range (5, n, 2):
            if n % i == 0 :
                return False
        return True

seed = [2, 3]


def checkprime(n):
    if n == 1 or n == 2 or n == 3:
        return True
    else:
        for i in seed:
            if n % i == 0:
                return False
        seed.append(n)
        return True


def checkprime_better(n):
    if n == 1 or n == 2 or n == 3:
        return True
    else:
        for i in seed:
            if i <= int(math.sqrt(n)):
                if n % i == 0:
                    return False
            else:
                break
        seed.append(n)
        return True




inp = int(input("inserisci un numero: "))

tempo = time.time()
for i in range(1, inp):
    if checkprime_better(i):
        print i
print("--- %s secondi ---" % (time.time()-tempo))
#print seed
