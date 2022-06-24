#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'performOperations' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER_ARRAY op
#

def performOperations(N, op):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = raw_input().rstrip().split()

    N = int(first_multiple_input[0])

    M = int(first_multiple_input[1])

    op = []

    for _ in xrange(M):
        op_item = int(raw_input().strip())
        op.append(op_item)

    result = performOperations(N, op)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
