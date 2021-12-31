def swap_zeros(arr):
    for j  in range(len(arr)):
        for i in range(len(arr)-1):
            if(arr[i] == 0):
                arr[i] , arr[i+1] = arr[i+1] , arr[i]
            
    print(arr)
            
swap_zeros([0,1,0,13,2])
#7 mins