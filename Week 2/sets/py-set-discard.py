n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    command = input().split(' ')       
    if(command[0] == "pop"):
        s.pop()
    elif(command[0] == "remove"):
        element = int(command[1])
        s.remove(element)
    elif(command[0] == "discard"):
        s.discard(int(command[1]))
print(sum(s))
    
