"""The following iterative sequence is defined for the set of positive integers

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""

SEARCH_CAP = 1000000
collatz_Length_List = []

#mung-ing (BRUTE FORCE RECURSION AHOY)
def method0():
    currCollatzCap = 0
    currCollatzCapSeqLength = 0

    for i in range(1, SEARCH_CAP):
        currSeqCurrPt = i
        currSeqLeng = 1

        if (i%10000 == 0):
            print(i)

        while (currSeqCurrPt != 1):
            if (currSeqCurrPt % 2 == 1):
                currSeqCurrPt = (3 * currSeqCurrPt) + 1
                currSeqLeng += currSeqLeng
            else:
                currSeqCurrPt = currSeqCurrPt / 2
                currSeqLeng += currSeqLeng
        if (currCollatzCapSeqLength <= currSeqLeng):
            currCollatzCap = i
            currCollatzCapSeqLength = currSeqLeng

    print (currCollatzCap)
    print (currCollatzCapSeqLength)


#slightly smarter recusion w/ results caching 
def countChain(n,currInd):
    if (n < currInd):                                   #check if we've entered previously computed chain
        return collatz_Length_List[int(n)-1]            #send off cached length if possible
    if (n==1):                                      
        return 1                                        #recursive base                                                                            
    if (n % 2 == 0):
        return (1 + countChain(n/2, currInd))           #Collatz even step
    else:
        return (1 + countChain(3 * n + 1, currInd))     #Collatz odd step

def method1():
    maxNum = 0                              #current maximal sequence number
    maxLen = 0                              #length of "maxNum" maximal chain
    for i in range(1, SEARCH_CAP):
        tmp = countChain(i,i)               #something went funky when I combined these lines
        collatz_Length_List.append(tmp)
        if (tmp >= maxLen):                 #if longer, update max & max length
            maxNum = i
            maxLen = tmp

    print("Maximal Collatz Number: " + str(maxNum))
    print("Collatz Chain Length:   " + str(maxLen))


#method0()    
method1()
