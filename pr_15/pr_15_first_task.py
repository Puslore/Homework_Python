from functools import singledispatchmethod


class Negator:
    @singledispatchmethod
    def neg(inpt):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register(int)
    def neg_int(inpt):
        return -inpt

    @neg.register(float)
    def neg_float(inpt):
        return -inpt

    @neg.register(bool)
    def neg_bool(inpt):
        return not inpt


print(Negator.neg(True))
print(Negator.neg(False))
print(Negator.neg(2))
print(Negator.neg(-10))
print(Negator.neg(24.8))
print(Negator.neg(-3.14))
# print(Negator.neg('stop!'))
