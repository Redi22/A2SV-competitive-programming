# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = map(int, input().split())
marks = list()
for i in range(x):
    marks.append(input().split())
marks = zip(*marks)
for i in marks:
    sum = 0
    for j in range(x):
        sum += float(i[j])
    print(sum / x)
