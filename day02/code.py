with open('input.txt') as d:
    data = d.read().splitlines()

lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
pwd = ''

for line in data:
    y = 1
    x = 1
    for char in line:
        if char == 'U' and y != 0:
            y -= 1
        elif char == 'R' and x != 2:
            x += 1
        elif char == 'D' and y != 2:
            y += 1
        elif char == 'L' and x != 0:
            x -= 1
    pwd += f'{lst[y][x]}'

lst2 = [
    ['0', '0', '1', '0', '0', ],
    ['0', '2', '3', '4', '0', ],
    ['5', '6', '7', '8', '9', ],
    ['0', 'A', 'B', 'C', '0', ],
    ['0', '0', 'D', '0', '0', ]
]

pwd2 = ''
for line in data:
    y2 = 2
    x2 = 0
    for char in line:
        if char == 'U' and y2 != 0:
            if lst2[y2-1][x2] != '0':
                y2 -= 1
        elif char == 'R' and x2 != 4:
            if lst2[y2][x2+1] != '0':
                x2 += 1
        elif char == 'D' and y2 != 4:
            if lst2[y2+1][x2] != '0':
                y2 += 1
        elif char == 'L' and x2 != 0:
            if lst2[y2][x2-1] != '0':
                x2 -= 1
    pwd2 += f'{lst2[y2][x2]}'
print(f'Part 1: {pwd}, Part 2: {pwd2}')
