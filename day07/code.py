get_sets_of_4_digits = lambda inp: [f'{char}{inp[index+1]}{inp[index+2]}{inp[index+3]}' for index, char in enumerate(inp[:-3])]
get_sets_of_3_digits = lambda inp: [f'{char}{inp[index+1]}{inp[index+2]}' for index, char in enumerate(inp[:-2])]
is_abba = lambda inp: True if inp[:2][::-1] == inp[2:] and inp[0] != inp[1] else False
is_aba = lambda inp: True if inp[0] == inp[2] and inp[0] != inp[1] else False
return_bab = lambda inp: f'{inp[1]}{inp[0]}{inp[1]}'


def get_hypernet_sequences(inp):
    hypernets = []
    normal_text = []
    text = ''
    for char in inp:
        if char == '[':
            normal_text.append(text)
            text = ''
        elif char == ']':
            hypernets.append(text)
            text = ''
        else:
            text += char
    normal_text.append(text)
    return normal_text, hypernets


def supports_tls(inp):
    boolean = False
    normal_text = get_hypernet_sequences(inp)[0]
    hypernets = get_hypernet_sequences(inp)[1]
    for text in normal_text:
        sets = get_sets_of_4_digits(text)
        for s in sets:
            if is_abba(s):
                boolean = True
                break
    for text in hypernets:
        sets = get_sets_of_4_digits(text)
        for s in sets:
            if is_abba(s):
                boolean = False
                break
    return boolean


def supports_ssl(inp):
    boolean = False
    normal_text = get_hypernet_sequences(inp)[0]
    hypernets = get_hypernet_sequences(inp)[1]
    bab = []
    for text in normal_text:
        sets = get_sets_of_3_digits(text)
        for s in sets:
            if is_aba(s):
                bab.append(return_bab(s))
    for text in hypernets:
        for s in bab:
            if s in text:
                boolean = True
                break
    return boolean


with open('input.txt') as d:
    data = d.read().splitlines()

counter = 0
counter2 = 0
for line in data:
    if supports_tls(line):
        counter += 1
    if supports_ssl(line):
        counter2 += 1

print(f'Part 1: {counter}, Part 2: {counter2}')
