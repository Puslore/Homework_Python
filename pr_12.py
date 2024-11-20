# Task 1
class BankAccount:
    def __init__(self, balance=1000):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError('not enough money')

        self._balance -= amount

    def __str__(self):
        return f'Bank balance: {self._balance}'


def intro_1():
    print('Please choose operation:\n1)increase money\n2)decrease money\nYou must in\put only 1 or 2 as numbers')
    try:
        operation = int(input())
        if operation == 1:
            amount = int(input('input amount of deposit: '))
            balance = BankAccount()
            balance.deposit(amount)
            print(f'Successfully deposited {amount}! Your current balance is {balance}')

        elif operation == 2:
            amount = int(input('input decrease amount: '))
            balance = BankAccount()
            balance.withdraw(amount)
            print(f'Successfully decreased by {amount}! Your current balance is {balance}')

        else:
            raise ValueError('Incorrect operation number')

    except Exception as err:
        print(f'ERROR: {err}. Please check your input\n')
        intro_1()


# intro_1()



# Task 2-------------------------------------------------------------------------------
class User:
    def __init__(self, name, age):
        if name_check(name):
            self._name = name

        else:
            raise ValueError('Incorrect name')

        if age_check(age):
            self._age = age

        else:
            raise ValueError('Incorrect age')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if name_check(new_name):
            self._name = new_name

        else:
            raise ValueError('Incorrect name')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if age_check(new_age):
            self._age = new_age

        else:
            raise ValueError('Incorrect age')

    def __str__(self):
        return f'name: {self.name}, age: {self.age}'


def name_check(name):
    return isinstance(name, str) and name != ''

def age_check(age):
    return isinstance(age, int) and age in range(0, 111)


user = User('Alex', 43)
print(user)
user.age = 110
print(user)
user.name = 'Vasya Pupkin'
print(user)



# Task 3-------------------------------------------------------------------------------
class IPAddress:
    def __init__(self, ipaddress):
        if ip_check(ipaddress) == 1:
            self.ipaddress = ipaddress

        elif ip_check(ipaddress) == 2:
            self.ipaddress = '.'.join(str(_) for _ in ipaddress)

        else:
            raise ValueError

    @property
    def ip_address(self):
        return self.ipaddress

    @ip_address.setter
    def ip_address(self, ipaddress):
        self.ipaddress = ipaddress

    def __str__(self):
        return f'{self.ipaddress}'


def ip_check(ip):
    if isinstance(ip, str):
        return 1

    elif isinstance(ip, list) or isinstance(ip, set):
        return 2

    else:
        return 0


ip_1 = [192, 255, 255, 21]
ip_2 = '192.176.175.26'

address1 = IPAddress(ip_1)
address2 = IPAddress(ip_2)

print(address1)
print(address2)
print(repr(address1))
print(repr(address2))



# Task 4-------------------------------------------------------------------------------
from functools import total_ordering


@total_ordering
class Word:
    def __init__(self, word):
        if not isinstance(word, str):
            raise ValueError('word must contain only letters like "Abcde"')
        self.word = word

    @property
    def word_(self):
        return self.word

    @word_.setter
    def word_(self, word):
        self.word = word

    def __str__(self):
        if not isinstance(self.word, str):
            raise NotImplemented
        return str(self.word)

    def __eq__(self, other):
        if not isinstance(self.word, str):
            raise NotImplemented
        return self.word == other.word

    def __lt__(self, other):
        if not isinstance(self.word, str):
            raise NotImplemented
        return self.word < other.word


word_1 = 'Abcd'
word_2 = 'Abs'

word_1_cls = Word(word_1)
word_2_cls = Word(word_2)

print(repr(word_1_cls))
print(word_2_cls)

print(word_1_cls == word_2_cls)
print(word_1_cls != word_2_cls)
print(word_1_cls < word_2_cls)
print(word_1_cls > word_2_cls)
print(word_1_cls <= word_2_cls)
print(word_1_cls >= word_2_cls)



# Task 5-------------------------------------------------------------------------------
class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __add__(self, other):
        params_list = [self.proteins,  other.proteins, self.fats,  other.fats, self.carbohydrates,  other.carbohydrates]
        if check_input(params_list):
            return FoodInfo(self.proteins + other.proteins, self.fats + other.fats, self.carbohydrates + other.carbohydrates)

        else:
            raise NotImplemented

    def __mul__(self, num):
        params_list = [self.proteins, self.fats, self.carbohydrates]
        if check_input(params_list) and (isinstance(num, int) or isinstance(num, float)):
            return FoodInfo(self.proteins * num, self.fats * num, self.carbohydrates * num)

        else:
            raise NotImplemented

    def __truediv__(self, num):
        params_list = [self.proteins, self.fats, self.carbohydrates]
        if check_input(params_list) and (isinstance(num, int) or isinstance(num, float)):
            return FoodInfo(self.proteins / num, self.fats / num, self.carbohydrates / num)

    def __floordiv__(self, num):
        params_list = [self.proteins, self.fats, self.carbohydrates]
        if check_input(params_list) and (isinstance(num, int) or isinstance(num, float)):
            return FoodInfo(self.proteins // num, self.fats // num, self.carbohydrates // num)

    def __str__(self):
        return f'proteins: {self.proteins}\nfats; {self.fats}\ncarbohydrates: {self.carbohydrates}'


def check_input(list_):
    return True if all(True if isinstance(_, int) or isinstance(_, float) else False for  _ in list_) else False


banana = FoodInfo(2, 20, 300)
chocolate = FoodInfo(6, 38, 540)

print(banana + chocolate)
print(banana * 2)
print(banana / 4)
print(banana // 87)
print(chocolate * 3)
print(chocolate / 2)
print(chocolate // 4)
