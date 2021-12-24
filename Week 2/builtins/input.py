# Enter your code here. Read input from STDIN. Print output to STDOUT
val , target = map(int , input().split())
poly = input()
xs = [ x.strip().replace('^','**') for x in poly.split('+') ]
print(target == sum( [eval(n.replace('x', str(val))) for n in xs] ))
