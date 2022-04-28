"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import timeit #used to test algorithmic efficiency

#The slightly less stupid euclids method
"""a = m^2 - n^2, b = 2mn, c = m^2 + n^2; m > n > 0;"""
def method1():
    foundFlag = False
    for n in range(1,100):
        for m in range(n, 100):
            if (2*m*(m+n)==1000):
                print((m*m-n*n)*(2*m*n)*(m*m+n*n))
                foundFlag = True
            if (foundFlag == True):
                break
        if (foundFlag == True):
            break

#the stupid munging method
def method0():
    boundingNum = 1000
    foundFlag = False
    foundA = 0
    foundB = 0
    foundC = 0
    for i in range(1,boundingNum+1):
        for j in range(i,boundingNum+1):
            for k in range (j,boundingNum+1):
                if (i*i + j*j == k*k):
                    if (i + j + k == boundingNum):
                        foundA = i
                        foundB = j
                        foundC = k    
                        foundFlag = True
                if (foundFlag == True):
                    break
            if (foundFlag == True):
                break
        if (foundFlag == True):
            break

    print("A = " + str(foundA) + "  B = " + str(foundB) + "  C = " + str(foundC) + "  Product = " + str(foundA*foundB*foundC))

print("runtime: " + str(timeit.timeit(method1, number=1))[0:7] + " seconds")
print("runtime: " + str(timeit.timeit(method0, number=1))[0:7] + " seconds")

