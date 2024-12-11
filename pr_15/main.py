from datetime import datetime
from functools import singledispatchmethod
import pytz


class BirthInfo:
    @singledispatchmethod
    def __init__(self):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(datetime)
    def __init__datetime(self, date):
        self.birth_time = date

    @__init__.register(str)
    def __init__str(self, date):
        try:
            self.birth_time = datetime.strptime(date, '%Y-%m-%d')

        except ValueError:
            return ValueError('incorrect str')

    @__init__.register(list)
    def __init__list(self, date):
        if len(date) == 3:
            self.birth_time = datetime(*date)

        else:
            return ValueError('incorrect list')

    @__init__.register(set)
    def __init__set(self, date):
        if len(date) == 3:
            self.birth_time = datetime(*date)

        else:
            return ValueError('incorrect set')

    def age(self):
        now = datetime.now(tz=pytz.timezone('Asia/Irkutsk')).date()
        years = now.year - self.birth_time.year

        last_birthday = self.birth_time.replace(year=now.year).date()
        if self.birth_time.month == 2 and self.birth_time.day == 29:
            while not leap_year(last_birthday.year):
                last_birthday = last_birthday.replace(year=last_birthday.year - 1)

        if last_birthday > now:
            years -= 1

        return years

    def days_until_birthday(self):
        now = datetime.now(tz=pytz.timezone('Asia/Irkutsk')).date()

        # Я решил, сделать так, что если человек родился 29.02, а следующий год не високосный, то день рождения считать 28.02
        if self.birth_time.month == 2 and self.birth_time.day == 29:
            next_birthday = self.birth_time.replace(year=now.year, day=28).date()
            if leap_year(now.year + 1):
                next_birthday = self.birth_time.replace(year=now.year + 1).date()

        else:
            next_birthday = self.birth_time.replace(year=now.year).date()

        if next_birthday < now:
            next_birthday = next_birthday.replace(year=next_birthday.year + 1)

        return (next_birthday - now).days


def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# тут тест задания из дз
# print(BirthInfo(datetime(2004, 2, 29)).age())
# print(BirthInfo(datetime(2004, 2, 29)).days_until_birthday())
# print(BirthInfo('2010-08-11').age())
# print(BirthInfo([2015, 6, 6]).age())
