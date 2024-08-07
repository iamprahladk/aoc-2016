import hashlib

inp = 'uqwqemis'
counter = 0
counter2 = 0
counter3 = 0
pwd = ''
complete_pwd = ''
pwd2 = ['' for n in range(8)]
indexes = [0, 1, 2, 3, 4, 5, 6, 7]
can_break = False
while not can_break:
    counter += 1
    updated_inp = inp + str(counter)
    md5 = hashlib.md5(updated_inp.encode()).hexdigest()
    if md5.startswith('00000'):
        try:
            sixth_digit = int(md5[5])
        except ValueError:
            continue
        seventh_digit = md5[6]
        pwd += f'{sixth_digit}'
        if sixth_digit in range(8) and sixth_digit in indexes:
            pwd2[sixth_digit] = seventh_digit
            counter2 += 1
            indexes.remove(sixth_digit)
    for char in pwd2:
        if char != '':
            counter3 += 1
    if counter3 == 8:
        can_break = True
    else:
        counter3 = 0
    if len(pwd) == 8:
        complete_pwd = pwd
pwd2_updated = ''
for char in pwd2:
    pwd2_updated += char
print(f'Part 1: {complete_pwd}, Part 2: {pwd2_updated}')
