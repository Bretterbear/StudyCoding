"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import timeit                           #used to test algorithmic efficiency
import math                             #needed for floor func

#same reasonably efficient primality tester used in problem 7
def isPrime(num):
    if (num==1):
        return False
    elif (num < 4):
        return True
    elif (num % 2 == 0):
        return False
    elif (num < 9):
        return True
    elif (num % 3 == 0):
        return False
    else:
        r = math.floor(math.sqrt(num))
        f = 5
        while (f <= r):
            if (num % f == 0):
                return False
            if (num % (f+2) == 0):
                return False
            f += 6
        return True

#no real way around this, primality test & add if prime. Sometimes you've just gotta do work.
#only tweak on this is if we're doing arbitary summing points, precompute prime list to an arbitrary threshhold...or make it dynamic for queries repeated.
def method0():
    sumPoint = 2000000
    primeSum = 0

    for i in range(1,sumPoint):
        if (isPrime(i)==True):
            primeSum = primeSum + i
    print(primeSum)

method0()
