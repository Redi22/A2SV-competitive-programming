def compare(ch):
    return [
            ch.isdigit(),
            ch.isupper(),
            ch.isdigit() and int(ch) % 2 == 0,
            ord(ch)
            ]

s = input()
sorted_s = sorted(s,key = compare)
print(''.join(sorted_s))

