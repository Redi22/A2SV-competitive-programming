def do_pattern_print(n):
    pattern = ""
    for i in range(1 , n+1):
        temp =  2 if i % 2 == 0 else 3
        for j in range(temp):
            if( i % 2 == 0):
                pattern += "  ##"
            else:
                pattern += "##  "
            
        print(pattern)
        pattern = ""
            

do_pattern_print(7)
#6: 22