"""Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?"""

latticeSize = 20

#Recursion Method
def recurseCountPaths(x,y):
    if ((x==0) or (y==0)):
        print("PATH ENDING")
        return 1

    print(str(x) + "-" + str(y))
    
    return recurseCountPaths(x-1, y) + recurseCountPaths (x, y - 1)

def method0():
    count = recurseCountPaths(latticeSize, latticeSize)
    print(count)

method0()

#Problem: recursion method will suffer from memory bloat as grid size increeases;
#Given it's a discrete grid & esp a sqwuare grid, we have a combinatorial solution for this: the routing possibility space for a lattice like this is 2n choose n
#in this case that's 40 choose 20
