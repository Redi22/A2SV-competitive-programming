# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

s, k  = input().split()
k = int(k)

for i in range(1 ,k+1):
    word_list = list(combinations(sorted(s), i))
    for word in word_list:
        print("".join(word))