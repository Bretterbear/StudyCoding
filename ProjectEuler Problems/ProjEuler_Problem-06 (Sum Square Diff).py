#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import timeit #used to test algorithmic efficiency

#Method 1 - The Thinking Man's method; using Gauss' Sum algorithm
def method1():
    limit = 100
    square_sum = limit*(limit+1)/2
    sum_squares = (2*limit+1)*(limit+1) * limit / 6
    difference = square_sum**2 - sum_squares
    print(differecne)

#Method 0 - The ugly brute force method
def method0():
    n = 100

    sumOfSquares = 0
    squareOfSums = 0

    for i in range(1,n+1):
        sumOfSquares += i*i
        squareOfSums += i

    squareOfSums = squareOfSums**2

    difference = squareOfSums - sumOfSquares

    print(difference)

print(timeit.timeit(method0, number=1))
print(timeit.timeit(method1, number=1))
