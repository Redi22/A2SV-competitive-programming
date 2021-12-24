# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    a , b =input().split()
    try:
        print(int(a) // int(b))
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:" , e)
    
