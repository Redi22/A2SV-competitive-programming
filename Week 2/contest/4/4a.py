def do_pattern_print(n):
    pattern_line = "1"
    for i in range(1,n+1):
        if(i != 1):
            for j in range(1, i+1):
                pattern_line += str(j)
            pattern_line += pattern_line[:-1][::-1]
        print(pattern_line.center(n*2 , "-"))
        pattern_line = ""
            

do_pattern_print(3)
#14 mins