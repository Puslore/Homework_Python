# Task 7

import re


def make_buffer_list(number, role, phrase):
    mbl = [f'{number}{role}', phrase.strip(role)]
    return mbl

with open('roles.txt', 'r', encoding='utf-8') as file:
    # creating roles list
    roles = [f'{file.readline()}:' for _ in range(26)]
    roles.pop(0)
    # db - dict with roles-keys and phrases-values
    db = {_: [] for _ in roles}
    # regular expression for easier roles sorting
    reg = r'^[А-ЯЁа-яё ]*:'
    file.readline()
    # creating list with all lines from text
    all_lines = [''.join(x).strip('\n') for x in file.readlines()]
    buffer_list = []
    cnt = 0
    key = ''
    buffer_phrase = ''

    # trying to solve task with for-cycle
    for phrase in all_lines:
        role = re.findall(reg, phrase)
        if role != '':
            cnt += 1
            buffer_list.append(make_buffer_list(cnt, role, phrase))
            key = cnt - 1
            buffer_phrase = phrase

        elif role == '':
            buffer_list[key][1].append(phrase)
            buffer_phrase = ''


print(buffer_list)
