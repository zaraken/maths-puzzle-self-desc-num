#!/usr/bin/env python
"""
This script restricts the number of candidate solutions
based on sum invariants and permutations
to solve and time 
a maths puzzle - The self descriptive number
Input is hardcoded.
"""

#author :Nikoaly Manolov
#license:GNU GPL Version 3
#==================================================

def increment(number, digit, budget, base, check_all):
    if budget == 0:
        cnt_num = getCount(number,base)
        if check(cnt_num, base):
            print '     ', ' num=', cnt_num + [0]
            return True
    elif digit == base-2: # last digit, must consume whole budget
        number[digit] = budget # because of sum invariant
        cnt_num = getCount(number,base)
        if check(cnt_num, base):
            print '     ', ' num=', cnt_num + [0]
            return True
    else:
        for val in range(min(budget,number[digit-1]),0,-1) if not digit==0 else range (budget-2,0,-1):
            number[digit] = val
            if increment(list(number), digit+1, budget-val, base, check_all) and not check_all:
                return True
    return False

def getCount(number,base):
    cnt_num = list()
    for i in range(base-1):
        cnt = number.count(i)
        if (i == 0): cnt+=1 # +1 for last zero
        cnt_num.append(cnt)
    return cnt_num

def check(number, base):
    if sum(number) > base:
        return False
    for i in range(base-1):
        cnt = number.count(i)
        if (i == 0): cnt+=1 # +1 for last zero
        if number[i] != cnt:
            return False
    return True

# base parameter, to keep implementation independent of representation
def test(base):
    number = [0 for i in range(base-1)]
    print
    print 'base=', base
    increment(number, 0, base, base, True)
    print '       time -> ',

if __name__ == '__main__':
    if not check([3,2,1,1,0,0], 7):
        print "Sanity check failed!"
    else:
        import timeit
        for base in [8, 15, 50]:
            #test(base)
            print (timeit.timeit("test(base)", setup="from __main__ import test; base=%d" % base, number=1))