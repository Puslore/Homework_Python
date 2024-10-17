# Task_1 var 3

import random as rand


names = [str(input('name: '))  for _ in range(int(input('value of students: ')))]

students = {i: str(sum([int(input(f"{i}'s {_+1} score: ")) for _ in range(3)])/3)[:5] for i in names}

for h, j in students.items(): print(h, j)

# ----------------------------------------------------------------------------------------------------------------
# Task_2

buyers = [input('name good quantity(Alex paper 3): ').split()  for _ in range(int(input('amount of purchases: ')))]
for j in buyers:
    j[2] = int(j[2])

db = {}


for i in buyers:
    if i[0] in db.keys():
        if i[1] in  db[i[0]]:
            db[i[0]][i[1]] += i[2]
        else:
            db[i[0]][i[1]] = i[2]
    else:
        db[i[0]] = {i[1]:i[2]}


db = dict(sorted(db.items(), key=lambda x: x[0]))
for _ in db.items():
    db[_[0]] = dict(sorted(_[1].items(), key=lambda z: z[0]))


for h in db.items():
    print(f'{h[0]}: {f"{h[1]}"[1:-1]}')
