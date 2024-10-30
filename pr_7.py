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
