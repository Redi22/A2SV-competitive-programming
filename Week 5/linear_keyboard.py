t = int(input())
for i in range(t):
    keyboard = input()
    keyboard = [i for i in keyboard]
    word = input()
    key_to_pos = {keyboard[i]: i+1 for i in range(len(keyboard))}
    init_pos = key_to_pos[word[0]]
    dist = 0
    for i in range(1, len(word) -1):
        
        final_pos = key_to_pos[word[i]]
        # print(init_pos , final_pos)

        dist += abs(final_pos - init_pos)
        init_pos = final_pos
    print(dist)
    