#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def isDivisor(b, d):
    for i in b:
        if i % d != 0:
            return False
    return True


def lcm(a):
    if len(a) == 1:
        return a[0]
    
    gcd = math.gcd(a[0], a[1])
    lcm = a[0] * a[1]  // gcd

    for i in range(2, len(a)):
        gcd = math.gcd(lcm, a[i])
        lcm = lcm * a[i] // gcd
    return lcm

def getFactors(a, ending):
    mul = lcm(a)
    end = ending // mul
    if (ending / mul) % 1 == 0.0:
        end += 1

    factors = [mul * i for i in range(1, end)]
    return factors

def getTotalX(a, b):
    # Write your code here
    # Define all facors of a, ending with first element of b
    factors = getFactors(a, b[0])

    factors_divisor = [1 for i in factors if isDivisor(b=b, d=i)]
    return len(factors_divisor)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
