"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""


#Need redo; method is so wildly inefficient it breaks PE's policy on 1 min sol'ns
import math


def factorCount(testNum):
    numOfFactors = 0
    for i in range (1, int(testNum/2+1)):
        if (testNum % i == 0):
            numOfFactors = numOfFactors + 1
    return numOfFactors+1

#this is just a stupid let's make sure I know what the answer is so I can check correctness of sol'n in more clever sol'ns
def mainMethod():
    seekingFactorCount = 500
    testNum = 0
    currIndex = 1

    while (testNum < 999999999999):
        testNum = testNum+currIndex
        currIndex = currIndex + 1
        if (currIndex % 100 == 0):
            print("testing " + str(testNum))
        if (factorCount(testNum) > seekingFactorCount):
            print(testNum)
            return

#mainMethod()

#Proper Solution; wildly more efficient
def factorCount2(n):
    if (n % 2 == 0):
        n = n / 2
    divisors = 1
    facCount = 0
    while (n % 2 == 0):
        facCount += 1
        n = n / 2
    divisors = divisors * (facCount + 1)
    p = 3
    while (n != 1):
        facCount = 0
        while (n % p == 0):
            facCount += 1
            n = n / p
        divisors = divisors * (facCount + 1)
        p += 2
    return divisors

def findTriIndex(factor_lim):
    n = 1
    lnum, rnum = factorCount2(n), factorCount2(n+1)
    while (lnum * rnum < factor_lim):
        n += 1
        lnum, rnum = rnum, factorCount2(n+1)
    return n

index = findTriIndex(500)
triangle = (index * (index + 1)) / 2
print(triangle)