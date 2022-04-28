#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math #used in elegant solution
import timeit #used to test algorithmic efficiency

#Testing function for divisbility
def isDiv(currNum):
    for i in range(11,20):
        if (currNum % i != 0):
            return False
    return True

#Method 1 - Elegant method using prime factorization"
#Note that p list must include all primes up to your k
def method1():
    k=20
    N=1
    i=1
    p = [1,2,3,5,7,11,13,17,19,23]
    a = [0,0,0,0,0,0,0,0,0,0,0,0]
    check=True
    limit = math.sqrt(k)
    while (p[i] <= k):
        a[i] = 1
        if (check):
            if (p[i] <= limit):
                a[i] = math.floor( math.log(k,10) / math.log(p[i],10))
            else:
                check = False
        N = N * (p[i]**a[i])
        i+=1
    print(N)

#Method 0 - The "mung until no good" brute force method. Wildly inefficient. Included to see how long it would take to run.
def method0():
    minNum = 2521 #set by an increment on min 1-10 div num

    #snippet for valid upper bound to prevent inf loop
    maxBound = 1
    for i in range (10,20):
        maxBound *= i

    while (minNum <= maxBound): #core validation cycle
        if (isDiv(minNum)):
            print("min Div = " + str(minNum))
            break
        minNum += 1 #increment on nonDiv

#single run test of methodO (takes 90+ seconds as the core loop iterates...200M+ cycles for a total of ~1B+ comparisons ops
#print(timeit.timeit(method0, number=1)) 
print(timeit.timeit(method1, number=1))
