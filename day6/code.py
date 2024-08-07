def find_common_char(inp, boolean):
    CHARS = 'abcdefghijklmnopqrstuvwxyz'
    output = []
    for char in CHARS:
        counter = 0
        for letter in inp:
            if char == letter:
                counter += 1
        if counter != 0:
            output.append(f'{counter}{char}')
    output = sorted(output, reverse=boolean)
    return output[0][2]


with open('input.txt') as d:
    data = d.read().splitlines()

lst = [[line[n] for line in data] for n in range(len(data[0]))]
word = ''
word2 = ''
for sub_lst in lst:
    word += find_common_char(sub_lst, True)
    word2 += find_common_char(sub_lst, False)

print(f'Part 1: {word}, Part 2: {word2}')
