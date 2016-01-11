#!/usr/bin/env python
"""
This script uses brute force to solve and time 
a maths puzzle - The self descriptive number
Input is hardcoded.
"""

#author :Nikolay Manolov
#license:GNU GPL Version 3
#==================================================

def increment(number, base):
    for i in range(len(number)-1,-1,-1):
        if number[i] == base-1:
            number[i] = 0
        else:
            number[i] = number[i]+1
            return True
    return False # overflow

def check(number, base):
    if sum(number) > base:
        return False
    for i in range(base):
        if number[i] != number.count(i):
            return False
    return True
    
def test(base):
    number = [0 for i in range(base)]
    print 'base=', base
    while increment(number, base):
        if check(number, base):
            print '     ', ' num=', number
    print '       time -> ',

if __name__ == '__main__':
    if not check([3,2,1,1,0,0,0], 7):
        print "Sanity check failed!"
    else:
        import timeit
        for base in range(2,9):
            #test(base)
            print (timeit.timeit("test(base)", setup="from __main__ import test; base=%d" % base, number=1))