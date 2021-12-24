if __name__ == '__main__':
    N = int(input())
    new_list = []
    for i in range(N):
        command = input().split(' ')       
        if(command[0] == "insert"):
            new_list.insert(int(command[1]) , int(command[2]))
        elif(command[0] == "remove"):
            element = int(command[1])
            new_list.remove(element)
        elif(command[0] == "append"):
            new_list.append(int(command[1]))
        elif(command[0] == "sort"):
            new_list.sort()
        elif(command[0] == "pop"):
            new_list.pop()
        elif(command[0] == "reverse"):
            new_list.reverse()
        elif(command[0] == "print"):
            print(new_list)
        
