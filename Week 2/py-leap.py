def is_leap(year):
    leap = False
    leap = False
    if(year % 4 == 0):
        if(year  % 100 == 0):
            if(year % 400 == 0):
                leap = True
        else:
            leap = True 
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))