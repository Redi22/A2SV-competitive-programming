# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

word , k  = input().split(' ')
k = int(k)
word_list = list(permutations(word, k))
word_list.sort()
for word in word_list:
    print("".join(word))