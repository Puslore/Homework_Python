# Task 7

import re

from Cython.Compiler.Parsing import print_parse_tree

with open('roles.txt', 'r') as file:
    roles = [f'{file.readline()[:-1]}:' for _ in range(26)]
    roles.pop(0)
    db = {_: [] for _ in roles}
    reg = r'^[А-ЯЁа-яё ]*:'
    print(db)
    file.readline()
    cnt = 1

    #         db[name].append(f'{cnt}) {line.strip(name)}')

    while True:
        line = file.readline().strip('\n')
        if line == '': break
        name = ''.join(re.findall(reg, line))
        phrase = ''

        if name in line:
            phrase += f'{cnt}) {line.strip(name)}'
            continue

        elif name not in line:
            phrase += line

        cnt += 1


for i in db.items():
    print(i[0])
    for j in i[1]:
        print(j)
    print()