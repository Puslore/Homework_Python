# Task 7

import re


with open('roles.txt', 'r', encoding='utf-8') as file:
    roles = [f'{file.readline()[:-1]}:' for _ in range(26)]
    roles.pop(0)
    db = {_: [] for _ in roles}
    reg = r'^[А-ЯЁа-яё ]*:'
    file.readline()
    all_lines = [''.join(x).strip('\n') for x in file.readlines()]


