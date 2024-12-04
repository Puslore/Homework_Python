# Task 1
from abc import abstractmethod
from random import choice


str_ = 'abcdefgh'

class ChessPiece:
    def __init__(self, horizontal, vertical):
        if horizontal in str_:
            self.horizontal = horizontal

        else:
            raise ValueError('Check horizontal coords input')

        if vertical in range(1, 9):
            self.vertical = vertical

        else:
            raise ValueError('Check vertical coord input')

    @abstractmethod
    def can_move(self, horizontal, vertical):
        pass


class King(ChessPiece):
    def can_move(self, horizontal, vertical):
        # print(str_.find(horizontal))
        # print(str_.find(self.horizontal))
        if (str_.find(horizontal) in (str_.find(self.horizontal) - 1, str_.find(self.horizontal) + 1, str_.find(self.horizontal)))\
                and (vertical in (self.vertical-1, self.vertical+1, self.vertical)) \
                and horizontal in str_ and vertical in range(1,9):
            return True

        else:
            return "Figure can't move this way"

class Knight(ChessPiece):
    def can_move(self, horizontal, vertical):
        if ((str_.find(horizontal) in (str_.find(self.horizontal) - 1, str_.find(self.horizontal) + 1)) and (vertical in (self.vertical+2, self.vertical - 2))) \
                or ((str_.find(horizontal) in (str_.find(self.horizontal) - 2, str_.find(self.horizontal) + 2)) and (vertical in (self.vertical+1, self.vertical - 1))) \
                and horizontal in str_ and vertical in range(1,9):
            return True

        else:
            return "Figure can't move this way"


fig1 = [King('a', 1), King('b', 4), King('h', 8)]
fig2 = [Knight('a', 1), Knight('b', 2), Knight('c', 1),
        Knight('d', 4), Knight('e', 5), Knight('f', 7), ]

cnt = 1
for fig in fig1:
    inp_hor, inp_ver = input(f'{cnt}) Input figure coords where you wanna put it. Like as a 2, b 4 or g 8\n').split()
    inp_ver = int(inp_ver)
    print(f'{fig.can_move(inp_hor, inp_ver)}\n')
    cnt += 1

cnt = 1
for fig in fig2:
    inp_hor, inp_ver = input(f'{cnt}) Input figure coords where you wanna put it. Like as a 2, b 4 or g 8\n').split()
    inp_ver = int(inp_ver)
    print(f'{fig.can_move(inp_hor, inp_ver)}\n')
    cnt += 1



# ---------------------------------------------------------------------------------------
# Task 2
class Father:
    def __init__(self, mood='neutral'):
        self.mood = mood

    def greet(self):
        return 'Hello!'

    def be_strict(self):
        self.mood = 'strick'


class Mother:
    def __init__(self, mood='neutral'):
        self.mood = mood

    def greet(self):
        return 'Hi, Honey!'

    def be_kind(self):
        self.mood = 'kind'


class Daughter(Mother, Father):
    pass


class Son(Father, Mother):
    pass


print(Mother().greet())
print(Father().greet())
print(Daughter().greet())
print(Son().greet())



# ---------------------------------------------------------------------------------------
# Task 3
class USADate:
    def __init__(self, year, month, day):
        if all(True if isinstance(_, int) else False for _ in (year, month, day)):
            self.year = year
            self.month = month
            self.day = day

        else:
            raise ValueError('Incorrect date. It must be only integer-type')


    def format(self):
        return f'{self.month}-{self.day}-{self.year}'

    def iso_format(self):
        return f'{self.year}-{self.month}-{self.day}'


class ItalianDate(USADate):
    def format(self):
        return f'{self.day}/{self.month}/{self.year}'\

    def iso_format(self):
        return f'{self.year}/{self.month}/{self.day}'


date1 = USADate(2024, 12, 4)
print(date1.format())
print(date1.iso_format())

date2 = ItalianDate(2024, 12, 4)
print(date2.format())
print(date2.iso_format())
