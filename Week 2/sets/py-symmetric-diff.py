# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int , input().split()))
diff_set = list(a.symmetric_difference(b))
diff_set.sort()
for element in diff_set:
    print(element)
