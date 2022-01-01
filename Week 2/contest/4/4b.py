def do_pattern_print(n):
    pattern_line = "1"
    old_pattern = []
    for i in range(1,n+1):
        if(i != 1):
            for j in range(1, i+1):
                pattern_line += str(j)
            pattern_line += pattern_line[:-1][::-1]
        print(pattern_line.center(n*2 , "-"))
        old_pattern.append(pattern_line)
        pattern_line = ""
            
    for i in range((len(old_pattern) -2 ), -1 , -1):
        print(str(old_pattern[i]).center(n*2 , "-"))
do_pattern_print(3)
#6 mins