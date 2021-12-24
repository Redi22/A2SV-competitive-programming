# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
set_n = set(map(int, input().split()))
m = int(input())
set_m = set(map(int, input().split()))
set_n = set_n.union(set_m)
print(len(set_n))
