# Task 7

import re

from Cython.Compiler.Parsing import print_parse_tree

with open('roles.txt', 'r') as file:
    roles = [f'{file.readline()[:-1]}:' for _ in range(5)]
    roles.pop(0)
    db = {_: [] for _ in roles}
    reg = r'^[А-ЯЁа-яё ]*:'
    # print(db)
    file.readline()
    cnt = 1

    while True:
        # file.readline()
        try:
            line = file.readline().strip('\n')
            if line == '': break
            name = ''.join(re.findall(reg, line))
            # print(name)
            # print(line)
            # print(db[name])
            db[name].append(f'{cnt}) {line.strip(name)}')
            # db[name].append(line)
            # db[name] += line.strip(name).strip('\n')
            # print(db[name])
            # print(line.strip(name))
            cnt += 1

        except:
            pass

for i in db.items():
    print(i[0])
    for j in i[1]:
        print(j)
    print()