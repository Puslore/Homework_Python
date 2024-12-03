# Task 1
from abc import abstractmethod
from functools import singledispatchmethod
from random import randint, choice


class Counter:
    def __init__(self, start=0):
        self._value = start

    def inc(self, value=1):
        if isinstance(value, int):
            self._value += value
            return f'Ваш счет: {self._value}'

        else:
            raise ValueError

    def dec(self, value=1):
        if isinstance(value, int):
            self._value -= value
            if self._value < 0:
                self._value = 0

            return f'Ваш счет: {self._value}'

        else:
            raise ValueError

    # def __str__(self):
    #     return f'Ваш счет: {self._value}'


class NonDecCounter(Counter):
    @abstractmethod
    def dec(self, value=1):
        pass


class LimitedCounter(Counter):
    def __init__(self, start=0, end=10):
        self._value = start
        self._end = end

    def inc(self, value=1):
        if isinstance(value, int):
            if self._value + value <= self._end:
                self._value += value
                return f'Ваш счет: {self._value}'

            else:
                return f'Ваш счет: {self._end}'

        else:
            raise ValueError


test = NonDecCounter(4)
print(test.dec(5))
print(test.inc(5))

test2= LimitedCounter(5, 11)
print(test2.dec(2))
print(test2.inc(20))
print(test2.inc(3))

test3 = Counter(2)
print(test3.inc(5))
print(test3.dec(1))



# Task 2-------------------------------------------------------------------------------
class Bachelor:
    def __init__(self, firstName, lastName, group, averageMark):
        self._firstName = firstName
        self._lastName = lastName
        self._group = group
        self.averageMark = averageMark

    def getScholarship(self):
        return f'{self._firstName} {self._lastName}. Стипендия: 10000' if \
        self.averageMark == 5 else f'{self._firstName} {self._lastName}. Стипендия: 5000' if \
        self.averageMark > 3 else f'{self._firstName} {self._lastName}. Профорг лишил вас стипендии:('


class Undergraduate(Bachelor):
    def getScholarship(self):
        return f'{self._firstName} {self._lastName}. Стипендия: 15000' if \
            self.averageMark == 5 else f'{self._firstName} {self._lastName}. Стипендия: 7500' if \
            self.averageMark > 3 else f'{self._firstName} {self._lastName}. no.'


student_names = ['Вася', 'Коля', 'Петя', 'Данил', 'Святослав']
student_surnames = ['Пупкин', 'Чернов', 'Ежевичкин', 'Белов', 'Серов']
student_marks = [randint(1, 5) for _ in range(10)]
student_groups = [randint(1, 3) for _ in range(10)]
students = [Bachelor(choice(student_names), choice(student_surnames),
                     choice(student_groups), choice(student_marks)) for _ in range(3)]

students_2 = [Undergraduate(choice(student_names), choice(student_surnames),
                     choice(student_groups), choice(student_marks)) for _ in range(3)]

for i in students:
    print(i.getScholarship())
for i in students_2:
    print(i.getScholarship())



# Task 3-НЕ СДЕЛАНО------------------------------------------------------------------------------
class Product:
    def __init__(self, name, cost, mass):
        if isinstance(name, str) and (isinstance(cost, int) or
        isinstance(cost, float)) and (isinstance(mass, int) or
        isinstance(mass, float)):
            self.__name = name
            self.__cost = cost
            self.__mass = mass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        self.__cost = cost

    @property
    def mass(self):
        return self.__mass

    @mass.setter
    def mass(self, mass):
        self.__mass = mass


class Buy(Product):
    def __init__(self, good, amount):
        self.__amount = amount
        self.__all_cost = self.__amount * good.cost
        self.__all_mass = self.__amount * good.mass

    @property
    def all_cost(self):
        return self.__all_cost

    @property
    def all_mass(self):
        return self.__all_mass


class Check(Buy):
    def __init__(self, product):
        self.__buy_cost = product.all_cost
        self.__buy_mass = product.all_mass

    def __str__(self):
        return f'Position: {self.__name}\nCost: {self.__cost}\nMass: {self.__mass}\n---  ---\nAmount: {self.__amount}\nTotal mass: {self.__all_mass}\n\nTotal cost: {self.__all_cost}'


banana = Product('Banana', 10, 0.5)
banana_buy = Buy(banana, 10)
banana_check = Check(banana_buy)
print(banana_check)
# print(Check(banana_buy))