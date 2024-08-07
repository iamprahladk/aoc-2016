def is_triangle(side1, side2, side3):
    lst = sorted([side1, side2, side3])
    if lst[0] + lst[1] > lst[2]:
        return True
    else:
        return False


with open('input.txt') as d:
    data = [n.split() for n in d.read().splitlines()]

count = 0
lst1 = []
lst2 = []
lst3 = []

for line in data:
    s1, s2, s3 = int(line[0]), int(line[1]), int(line[2])
    if is_triangle(s1, s2, s3):
        count += 1
    lst1.append(s1)
    lst2.append(s2)
    lst3.append(s3)

count2 = 0
lst1 = [lst1[i:i+3] for i in range(0, len(lst1), 3)]
lst1 += [lst2[i:i+3] for i in range(0, len(lst2), 3)]
lst1 += [lst3[i:i+3] for i in range(0, len(lst3), 3)]


for line in lst1:
    s1, s2, s3 = int(line[0]), int(line[1]), int(line[2])
    if is_triangle(s1, s2, s3):
        count2 += 1
print(f'Part 1: {count}, Part 2: {count2}')
