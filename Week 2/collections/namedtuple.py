# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
size = int(input())
data = input().split()  
mark_sum = 0
Student = namedtuple('Student' , " ".join(data))
for i in range(size):
    studInfo = input().split()
    mark_sum += int(Student(*studInfo).MARKS)
print(mark_sum/size)
