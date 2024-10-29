# Task 7

import re


with open('roles.txt', 'r') as file:
    roles = [f'{file.readline()[:-1]}:' for _ in range(26)]
    roles.pop(0)
    db = {_: [] for _ in roles}
    reg = r'^[А-ЯЁа-яё ]*:'
    # print(db)
    file.readline()
    cnt = 0
    buffer_line = ''

    while True:
        cnt += 1
        line = file.readline().strip('\n')
        if line == '': break
        name = ''.join(re.findall(reg, line))

        # if buffer_line != '':
        #     db[''.join(re.findall(reg, buffer_line))].append(f'{cnt}) {buffer_line.strip(name)}')

        if name != '' and name in roles:
            # db[name].append(f'{cnt}) {line.strip(name)}')
            pers_name = name
            phrase = ''
            db[pers_name].append(f'{cnt}) {line.strip(name)}')
            continue

        elif name == '':
            db[pers_name][-1] += f'{line.strip(name)}'

        while ''.join(re.findall(reg, line)) == '':
            # try:
            #     # print(db[pers_name])
            #     db[pers_name].pop()
            # except IndexError:
            #     pass
            line = file.readline().strip('\n')
            buffer_line = line
            if ''.join(re.findall(reg, line)) == '':
                phrase += line
            elif ''.join(re.findall(reg, line)) != '' and ''.join(re.findall(reg, line)) in roles:
                db[''.join(re.findall(reg, line))].append(f'{cnt+1}) {line.strip("".join(re.findall(reg, line)))}')
                continue

        # if ''.join(re.findall(reg, line)) != '':
        #     db[pers_name].append(f'{cnt}) {line.strip(pers_name)}')

        # if ''.join(re.findall(reg, line)) == '':
        db[pers_name][-1] += f'{phrase}'




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