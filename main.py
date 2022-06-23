#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    finalresult = []
    maxrecord = 0
    minrecord = 0

    for x in range(2):
        finalresult.append(scores[0])

    for x in scores:
        if x > finalresult[0]:
            finalresult[0] = x
            maxrecord = maxrecord + 1
        if x < finalresult[1]:
            finalresult[1] = x
            minrecord = minrecord + 1

    finalresult[0] = maxrecord
    finalresult[1] = minrecord

    return(finalresult)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
