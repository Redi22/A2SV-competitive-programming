# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())
shoe_nums = Counter(map(int, input().split()))
m = int(input())
price_sum = 0
for i in range(m):
    s_size , s_price = map(int, input().split())
    if(shoe_nums[s_size] > 0):
        shoe_nums[s_size] -= 1
        price_sum +=s_price
print(price_sum)
    

