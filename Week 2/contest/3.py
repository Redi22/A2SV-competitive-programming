def do_pattern_print(n):
    for i in range(2):
        print( n * ( ((n-1) *"#").ljust(n, " ") ) )

do_pattern_print(4)


#another way
def do_pattern_print(num):
    x = num - 1
    for i in range(2):
        for j in range(1,num+1):
            print("#"*x,end="")
            print(" ",end="")
        print()
n = int(input())
do_pattern_print(n)