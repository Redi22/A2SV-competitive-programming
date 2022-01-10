# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int , input().split(' ')))
    nums = list(map(abs , nums))
    counted_nums = Counter(nums)
    unique_nums = 0
    for num , freq in counted_nums.items():
        if(num != 0):
            if(freq >= 2):
                unique_nums += 2
            else:
                unique_nums += freq
        else:
            unique_nums += 1
    print(unique_nums)
            