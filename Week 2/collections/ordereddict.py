# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
item_dict = OrderedDict()
n = int(input())
for i in range(n):
    item = input().split()
    item_name = " ".join(item[:-1])
    item_price = item[-1:]
    if item_name in item_dict.keys():
        item_dict[item_name] += int(item_price[0])
    else:
        item_dict[item_name] = int(item_price[0])

for i in item_dict.items():
    print(*i)
