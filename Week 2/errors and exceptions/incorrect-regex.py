# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for i in range(n):
    m = input()
    try:
        Compile_regex = re.compile(m)
        print(True)
    except:
        print (False)
