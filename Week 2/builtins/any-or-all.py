# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
nums = input().split()
print (all([int(i)>0 for i in nums]) and any([''.join(reversed(j)) == j for j in nums]))
