# Task 7

import re


with open('roles.txt', 'r') as file:
    roles = [f'{file.readline()[:-1]}:' for _ in range(26)]
    roles.pop(0)
    db = {_: [] for _ in roles}
    reg = r'^[А-ЯЁа-яё ]*:'
    # print(db)
    file.readline()
    cnt = 1

    while True:
        line = file.readline().strip('\n')
        if line == '': break
        name = ''.join(re.findall(reg, line))
        phrase = line

        if name != '' and name in roles:
            # db[name].append(f'{cnt}) {line.strip(name)}')
            pers_name = name
            phrase = line

        elif name == '':
            while ''.join(re.findall(reg, line)) == '':
                phrase += line
                line = file.readline().strip('\n')

        db[pers_name].append(f'{cnt}) {phrase.strip(pers_name)}')
        cnt += 1



        # print(phrase)
        # print(db)

        # if name != '':
        #     phrase = f'{cnt}) {line.strip(name)}'
        #     # line = file.readline().strip('\n')
        #
        #     # if ''.join(re.findall(reg, line)) != '':
        #     #     db[name].append(f'{cnt}) {line.strip(name)}')
        #     #     break
        #
        #     while ''.join(re.findall(reg, line)) == '':
        #         line = file.readline().strip('\n')
        #         phrase += line

        # print(phrase)
        # db[name].append(f'{cnt}) {phrase.strip(name)}')

for i in db.items():
    print(i[0])
    for j in i[1]:
        print(j)
    print()