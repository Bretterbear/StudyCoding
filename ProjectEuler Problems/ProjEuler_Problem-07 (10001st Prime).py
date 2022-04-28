#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import timeit #used to test algorithmic efficiency
import math #needed for floor func

#Ultra Lazy method for prime test; runs wildly inefficiently
def isPrime(num):
    for i in range(2,num-1):
        if (num % i == 0):
            return False
    return True

#More efficient primality test method
def isPrime1(num):
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


#Method 0 - The ugle brett method for Munging Primes using the more efficient "isPrime1" primality test
#This is one of those hairy problems. since this is a one off, we're just discarding results as we go & stopping when we hit the nth prime.
#That said; if we were going to be doing this on a regular basis & were going to be grabbing arbitrary primes below a bound I'd edit as follows:
#Make a lookup table or I guess in python a dict would be ideal, just keep storing as we go up as needed. 
#or we precompute everything, make a seive of eratosthenese up to an arbitrary bounding numbers as set by the parameters of what larger program the module was in.
def method0():
    primesFound = 2
    currNum = 3
    target = 10001
    
    while (True):
        currNum += 2
        if isPrime1(currNum):
            primesFound += 1
        if primesFound >= target:
            break
        else:
            continue
    print(currNum)
