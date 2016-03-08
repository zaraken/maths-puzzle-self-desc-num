#!/usr/bin/env python
"""
This script restricts the number of candidate solutions
based on sum invariant (digit_sum == 10) 
and permutations (a solution can be built from any permutation
of the same digits if such exists)
to solve and time 
a maths puzzle - The self descriptive number
Input is hardcoded.
"""

#author :Nikolay Manolov
#license:GNU GPL Version 3
#==================================================

def increment(number, digit, budget, base, find_all):
    if budget == 0: # the budget has been exhaust, sum(number) == base is true
        cnt_num = getCount(number,base) # generate a new number that describes of the current
                                        # The idea is that the generated number describes all
                                        # numbers that are formed by the same set of digits
                                        # (including itself if it is a solution)
        if check(cnt_num, base):
            print '     ', ' num=', cnt_num + [0]
            return True
    elif digit == base-2: # last digit, must consume whole remaining budget
        number[digit] = budget # because of sum invariant
        cnt_num = getCount(number,base)
        if check(cnt_num, base):
            print '     ', ' num=', cnt_num + [0]
            return True
    else:   # Distribute budget starting from zero and passing the remainder right to the next digit
            # in decreasing volume from max to 0
        for val in range(min(budget,number[digit-1]),0,-1) if not digit==0 else range (budget-2,0,-1):
            number[digit] = val
            if increment(list(number), digit+1, budget-val, base, find_all) and not find_all:
                return True
    return False

def getCount(number,base):
    #cnt_num = list()
    #for i in range(base-1):
    #    cnt = number.count(i)
    #    if (i == 0): cnt+=1 # +1 for last zero
    #    cnt_num.append(cnt)
    cnt_num = [1] + [0]*(base-2)
    for i in range(base-1):
        cnt_num[number[i]] += 1
    return cnt_num

def check(number, base):
    #if sum(number) > base:
    #    return False
    if number[0] != 1 + number.count(0): return False # +1 for last zero
    return all(number.count(i)==number[i] for i in range(1, base-1))

# base parameter, to keep implementation independent of representation
def test(base, find_all):
    number = [0]*(base-1)
    print
    print 'base=', base
    increment(number, 0, base, base, find_all)
    print '       time -> ',

if __name__ == '__main__':
    import sys

    print "Usage: python {0} [starting_number upper_limit] [-find_all]".format(sys.argv[0])

    low = 5000
    high = 5001
    find_all = False
    if len(sys.argv) > 2:
        low = int(sys.argv[1])
        high = int(sys.argv[2])
        if len(sys.argv) > 3:
            find_all = "-find_all" == sys.argv[3]
    if not check(getCount([3,2,1,1,0,0], 7),7):
        print "Sanity check failed!"
    else:
        import timeit
        for base in range(low,high): #check all numbers in this range
            #test(base, find_all)
            print (timeit.timeit("test(base, find_all)", setup="from __main__ import test; base={0:d}; find_all={1}".format(base, find_all), number=1))