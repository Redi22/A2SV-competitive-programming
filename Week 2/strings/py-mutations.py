def mutate_string(string, position, character):
    # new_str = list(string)
    # new_str[position] = character
    # string = ''.join(new_str)
    return string[:position] + character + string[position+1:]
   
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)