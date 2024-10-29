# Task 1 var 3

import random


n, m = map(int, input().split())

img = [str(input()) for _ in range(n)]
print()
m_img = [str(input()) for _ in range(n)]

print(sum([1 if x[h] == y[h] else 0 for h in range(m)\
            for x, y in [i for i in zip(img, m_img)]]))

# -------------------------------------------------------------------------------
# Task 2
'''
я не справился, добился только заполнения поля минами
'''
# n, m, k = map(int, input().split())
n, m, k = 15, 20, 10
# mines = [[[x, y] for x, y in input().split()] for _ in range(k)]
mines = [(random.randint(0, 15), random.randint(0, 15)) for _ in range(k)]
_map = [[[] for _ in range(n)] for _ in range(m)]
# print(_map)
# print(mines)
for i in enumerate(_map):
    # print(i)
    for j in enumerate(i[1]):
        # pass
        # print(j)
        # print(j[0])
        if (i[0], j[0]) in mines: _map[i[0]][j[0]].append('*')
        # print(_map[i[0]][j[0]])

# f = [[(lambda i, j: ['*'] if _map[i[0]][j[0]] else [])(i, j) for j in enumerate(i)] for i in [enumerate(_map)][0]]
# print(f)

print(_map)
