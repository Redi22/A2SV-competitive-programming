# Enter your code here. Read input from STDIN. Print output to STDOUT
n ,m = input().split()
arr = list(map(int , input().split()))
setA = set(map(int , input().split()))
setB = set(map(int , input().split()))
happiness = 0
for i in arr:
    if i in setA:
        happiness += 1
    if i in setB:
        happiness -= 1
print(happiness)