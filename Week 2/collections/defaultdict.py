# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n , m = map(int,input().split())
nd = defaultdict(list)
md = defaultdict(list)
for i in range(1, n+1, 1):
    my_input = input()
    nd[my_input].append(i)
for i in range(1 ,m+1 , 1):
    my_input = input()
    md[my_input].append(i)
# nd = dict(nd)
print(nd , md)
for i in nd.items():
    print(*nd[i[0]])
for i in md.items():
    print(*md[i[0]])
