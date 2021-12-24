if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    first = arr[0]
    second = -101
    for i in range(1 , n):
        if(arr[i] < first):
            if(arr[i] > second):
                second = arr[i]
        elif(arr[i] > first):
            first , second = arr[i] , first 
    print(second)
    
