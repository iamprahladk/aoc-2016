def turn_right(direction):
    if direction == 'N':
        return 'E'
    elif direction == 'E':
        return 'S'
    elif direction == 'S':
        return 'W'
    else:
        return 'N'


def turn_left(direction):
    if direction == 'N':
        return 'W'
    elif direction == 'W':
        return 'S'
    elif direction == 'S':
        return 'E'
    else:
        return 'N'


move_north = lambda x, y: (x, y + 1)
move_east = lambda x, y: (x + 1, y)
move_south = lambda x, y: (x, y - 1)
move_west = lambda x, y: (x - 1, y)

with open('input.txt') as d:
    data = d.read().split(', ')

current_dir = 'N'
x_coor = 0
y_coor = 0

lst = []
boolean = True
for item in data:
    if item.startswith('L'):
        current_dir = turn_left(current_dir)
    else:
        current_dir = turn_right(current_dir)
    for n in range(int(item[1:])):
        if current_dir == 'N':
            x_coor, y_coor = move_north(x_coor, y_coor)
        elif current_dir == 'E':
            x_coor, y_coor = move_east(x_coor, y_coor)
        elif current_dir == 'S':
            x_coor, y_coor = move_south(x_coor, y_coor)
        else:
            x_coor, y_coor = move_west(x_coor, y_coor)
        if (x_coor, y_coor) in lst and boolean:
            print(f'Part 2: {x_coor + y_coor}')
            boolean = False
        else:
            lst.append((x_coor, y_coor))
print(f'Part 1: {x_coor + y_coor}')
