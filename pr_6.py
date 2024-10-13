# Task_1
import random as rand


# names = [str(input('name: '))  for _ in range(int(input('value of students: ')))]
# # students = {i: str(sum([rand.randint(0, 100) for _ in range(3)])/3)[:5] for i in names}
# students = {i: str(sum([int(input(f"{i}'s {_+1} score: ")) for _ in range(3)])/3)[:5] for i in names}
#
# for h, j in students.items(): print(h, j)

# ----------------------------------------------------------------------------------------------------------------
# Task_2

from collections import OrderedDict


# buyers = [input('name good quantity(Alex paper 3): ').split()  for _ in range(int(input('amount of purchases: ')))]
buyers = [['petr', 'paper', 4], ['petr', 'pens', 10], ['vlad', 'potato', 5], ['petr', 'paper', 2]]
# db = OrderedDict({i[0]: {i[1]: i[2]} for i in sorted(buyers, key=lambda x: x[0])})
db = [{i[0]: {i[1]: i[2]}} for i in sorted(buyers, key=lambda x: x[0])]
db_2 = {}

# for purchase in enumerate(db):
#     for i in range(purchase[-1:][0]):
#         db_2[purchase[1][0]] = {purchase[1][1]}

for purchase in buyers:
    db_2.update({purchase[0]:{purchase[1]: purchase[2]}}) if \
    db_2.get(purchase[0], True) == True else \
    db_2[purchase[0]][purchase[1]] += purchase[2] if \
    db_2[0].get(purchase[1], True) == True else \
    db_2[purchase[0]].update({purchase[1]: purchase[2]})

print(db)
print(db_2)
