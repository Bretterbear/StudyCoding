#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
import timeit #used to test algorithmic efficiency

#Integer Palindrome testing function (will not work on non-ints)
def isPalindrome(num):
    temp = num
    rev = 0
    while(num>0):
        rev = rev * 10 + num % 10
        num = num//10
    return (temp == rev)

#Function for printing result
def outputString(x,y,outputProduct):
    print("largest 3 Digit Palindrome Product is: " + str(outputProduct))
    print("Formed of: " + str(x) + " & " + str(y))

#Method 1 - Trivial Count-Up Method            
def method1():
    largestPalindrome = 0
    largestX = 0
    largestY = 0

    for x in range (100,999):
        for y in range (x,999): #inner loop starts at current outer loop index to avoid work repetition
            testProduct = x * y
            if (isPalindrome(testProduct)):
                if (testProduct > largestPalindrome):
                    largestPalindrome = testProduct
                    largestX = x
                    largestY = y
    #outputString(largestX,largestY,largestPalindrome)

#Method 2 - CountDown method
#Working down from top rather than up from bottom means we'll find a large palindrome faster
def method2():  
    largestPalindrome = 0
    largestA = 0
    largestB = 0

    a = 999
    while (a >= 100):
        b = 999
        while (b >= a):
            if a * b <= largestPalindrome:
                break
            if isPalindrome(a*b):
                largestPalindrome= a*b
                largestA = a
                largestB = b
            b -= 1
        a -= 1
    #outputString(largestA,largestB,largestPalindrome)

#Method 3 - Cheese method
#Explanation (this is an odd one): our palindrome is a product of 2 3 digit numbers, which means it's at least 6 digits long (a spit out result from method1, not proved here)
#since that's the case, we can write it as Pal = 100001x + 010010y + 001100z with x,y,&z being our palindromed digits
#we can pull out the prime factor 11 from that & use the fact that 11's got to be a prime factor of either A or B, allowing us to speed through
#I feel like there's a breakage case here if we started going above 999; but I'm not positive, and don't have time atm to verify.
def method3():  
    largestPalindrome = 0
    largestA = 0
    largestB = 0

    a = 999
    while (a >= 100):
        db = 0
        if (a % 11 == 0):
            b = 999
            db = 1
        else:
            b=990
            db = 11
        while (b >= a):
            if (a*b <= largestPalindrome):
                break
            if (isPalindrome(a*b)):
                largestPalindrome = a*b
                largestA = a
                largestB = b
            b -= db
        a -= 1    

#testing time efficiencies of various methods
print(timeit.timeit(method1, number=10))
print(timeit.timeit(method2, number=10))
print(timeit.timeit(method3, number=10))
