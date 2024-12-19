# Task 1
# big_chislo = 2 ** 74207281 - 1
X = 514229

def start():
    print('Input Pattern and Text like Pattern Text')
    k = input()
    if isinstance(k, str):
        pattern, text = k.split()

    else:
        raise ValueError('Check input. It must be only string')

    return pattern, text


def hash_(string_):
    res = 0
    for i, j in enumerate(string_):
        res += ord(j) * X ** i

    return res

def main():
    pattern, text = start()

    ans = []
    leng_t = len(text)
    leng_p = len(pattern)
    a = X ** (leng_p - 1)
    pat_hash = hash_(pattern)
    t_hash = hash_(text[leng_t - leng_p: leng_t])

    if pat_hash == t_hash:
        ans.append(leng_t - leng_p)

    for i in range(leng_t - leng_p):
        t_hash = (t_hash - a * ord(text[leng_t - i - 1])) \
                 * X + ord(text[leng_t - leng_p - i - 1])

        if pat_hash == t_hash:
            ans.append(leng_t - leng_p - i - 1)

    print(f'Index: {sorted(ans)[0]}')


main()



# ---------------------------------------------------------------------------------------
# Task 2
class ColoredPoint:
    def __init__(self, x, y, color):
        if all(True if isinstance(_, int) or isinstance(_, float) else False for _ in [x, y]):
            self._x = x
            self._y = y

        else:
            raise ValueError

        if isinstance(color, str):
            self._color = color

        else:
            raise ValueError

    @property
    def ret_x(self):
        return self._x

    @property
    def ret_y(self):
        return self._y

    @property
    def ret_col(self):
        return self._color

    def __eq__(self, other):
        if isinstance(other, ColoredPoint):
            return self._x == other._x and self._y == other._y

        else:
            raise NotImplemented

    def __ne__(self, other):
        if isinstance(other, ColoredPoint):
            return self._x != other._x and self._y != other._y

        else:
            raise NotImplemented

    def __hash__(self):
        return hash((self._x, self._y, self._color))


test1 = ColoredPoint(1, 1, 'brown')
test2 = ColoredPoint(1, 1, 'brown')
print(test1 == test2)
print(test1 != test2)
print(hash(test1))

test1 = ColoredPoint(14, 3, 'black')
test2 = ColoredPoint(4, 19, 'yellow')
print(hash(test1), hash(test2))
