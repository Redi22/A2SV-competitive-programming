# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
from itertools import combinations

n = int(input())
letters  = input().split()
k = int(input())

counter = 0
possible_outcomes = list(combinations(letters , k))
for out in possible_outcomes:
    if('a' in out):
        counter += 1
print(counter / len(possible_outcomes))
        