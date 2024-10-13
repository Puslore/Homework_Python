import random

m, n = map(int, input().split())

sum_list = [sum(random.randint(1, 15) for i in range(m)) for j in range(n)]
print(max(sum_list), sum_list.index(max(sum_list)))

# --------------------------------------------------------------------------------------------
# ненормальное решение

h = [t for t in enumerate((sum(random.randint(1, 15) for _ in range(m)) for _ in range(n)), start=1)]

print([f'{x} спортсмен: {y}' for x, y in h if (y == max(d for k, d in h))][0])
