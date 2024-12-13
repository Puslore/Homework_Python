# Task 1
def fib(n):
    first = 0
    second = 1
    nn = 0
    for i in range(n):
        yield nn
        nn = first + second
        first = second
        second = nn

l = [_ for _ in fib(30)]
print(l)



# ---------------------------------------------------------------------------------------
# Task 2
def simple_int(n):
    for i in range(2, n):
        if check(i) and n % i == 0:
            yield i

def check(num):
    if all(True if num % i != 0 or i in (1, num) else False for i in range(2, num)):
        return True

l = [_ for _ in simple_int(999)]
print(l)



# ---------------------------------------------------------------------------------------
# Task 3
def stepeni(num, step):
    for i in range(step+1):
        yield num ** i

w = [_ for _ in stepeni(2, 8)]
print(w)



# ---------------------------------------------------------------------------------------
# Task 4
def prostie_in_range(start, end):
    for i in range(start+1, end):
        if check(i):
            yield i

g = [_ for _ in prostie_in_range(2, 43)]
print(g)
