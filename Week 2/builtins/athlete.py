import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    nums = []

    for i in range(n):
        nums.append(list(map(int, input().rstrip().split())))

    k = int(input())
nums.sort(key=lambda x: x[k])
for i in range(n):
    print(*nums[i], end=" ")
    print()