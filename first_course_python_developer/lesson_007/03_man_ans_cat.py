# -*- coding: utf-8 -*-
# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# TODO здесь ваш код
from termcolor import cprint, colored
from random import randint


class Man:

    def __init__(self, name):
        self.fullness = 50
        self.name = name.title()
        self.house = None
        self.cat = None

    def __str__(self):
        return colored(f'Я - {self.name}, я сыт на {self.fullness}%', color='green')

    def eat(self):
        if self.house.food >= 10:
            cprint(f'{self.name} поел', color='blue')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint(f'У {self.name} нет еды (', color='red')

    def work(self):
        cprint(f'{self.name} сходил на работу', color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_mtv(self):
        cprint(f'{self.name} смотрел MTV', color='blue')
        self.fullness -= 10

    def clean_up_the_house(self):
        if self.fullness > 10:
            cprint(f'{self.name} убрад дом', color='blue')
            self.house.dirt -= 50
            self.fullness -= 10

    def feed_the_cat(self):
        if self.house.cat_food > 0:
            cprint(f'{self.name} покормил {self.cat.name}', color='blue')
            self.house.cat_food -= 10
            self.cat.fullness += 20
        else:
            cprint('В доме нет еды для кота', color='red')

    def take_a_cat(self, cat_name):
        cprint(f'{self.name} подобрал кота и дал ему кличку - {cat_name.name}', color='cyan')
        self.cat = cat_name
        cat_name.house = self.house

    def go_into_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint(f'{self.name} заехал в дом', color='cyan')

    def shopping(self):
        if self.house.money >= 50:
            cprint(f'{self.name} сходил в магазин за едой', color='blue')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint(f'У {self.name} кончились деньги', color='red')

    def cat_shopping(self):
        if self.house.money >= 50:
            cprint(f'{self.name} сходил в магазин за едой для {self.cat.name}', color='blue')
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            cprint(f'У {self.name} кончились деньги', color='red')

    def act(self):
        if self.fullness <= 0:
            cprint(f'{self.name} умер от голода', color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 20:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.cat_food < 30:
            self.cat_shopping()
        elif self.cat.fullness <= 40:
            self.feed_the_cat()
        elif self.house.dirt > 100:
            self.clean_up_the_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_mtv()


class House:
    def __init__(self):
        self.food = 10
        self.cat_food = 10
        self.money = 50
        self.dirt = 0

    def __str__(self):
        return colored(f'В доме осталось {self.food} еды и {self.money} денег', color='green')


class Cat:
    def __init__(self, name):
        self.fullness = 50
        self.house = None
        self.name = name

    def __str__(self):
        return colored(f'Я кот по имени - {self.name}, я сыт на {self.fullness} %', color='green')

    def sleep(self):
        cprint(f'{self.name} проспал весь день', color='blue')
        self.fullness -= 10

    def tear_up_wallpaper(self):
        cprint(f'{self.name} подрал обои', color='blue')
        self.fullness -= 10
        self.house.dirt += 5

    def cat_act(self):
        dice = randint(1, 6)
        if self.fullness <= 0:
            cprint(f'{self.name} умер от голода', color='red')
        elif dice % 2 == 0:
            self.tear_up_wallpaper()
        else:
            self.sleep()


liza = Cat('Лиза')
citizen = Man(name='Федя')
my_sweet_home = House()
citizen.go_into_the_house(my_sweet_home)
citizen.take_a_cat(liza)
for day in range(1, 366):
    print(f'============ день {day} ============')
    citizen.act()
    citizen.cat.cat_act()
    print('============= Итоги дня =============')
    print(citizen)
    print(citizen.cat)
    print(citizen.house)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
