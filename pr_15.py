# Task 1
from datetime import datetime
from functools import singledispatchmethod
import pytz


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



# ---------------------------------------------------------------------------------------
# Task 2
class BirthInfo:
    @singledispatchmethod
    def __init__(self, date):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(datetime)
    def __init__date_class(self, date):
        self.birth_time = date
        print(self.birth_time)

    @__init__.register(str)
    def __init__iso(self, date):
        self.birth_time = datetime(*date.split())
        print(self.birth_time)

    @__init__.register(list)
    def __init__list(self, date):
        self.birth_time = datetime(*date.split())
        print(self.birth_time)

    @__init__.register(set)
    def __init__list(self, date):
        self.birth_time = datetime(*date.split())
        print(self.birth_time)

    def age(self):
        return (datetime.now(tz=pytz.timezone('Asia/Irkutsk')).date() - self.birth_time.date()) / 365


print(BirthInfo(datetime(2023, 09, 22)).age())
# can work incorrect. I don't know how to fix that. There's troubles with datetime module

# a = datetime.now(tz=pytz.timezone('Asia/Irkutsk')).date()
# print(a)
# b = datetime(2000, 12, 14).date()
# print(b)
# print(a - b)
# print((datetime.now(tz=pytz.timezone('Asia/Irkutsk')).date() - datetime(2000, 12, 14).date()).)
