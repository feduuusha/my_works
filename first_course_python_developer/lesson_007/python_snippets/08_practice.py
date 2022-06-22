# -*- coding: utf-8 -*-

from random import randint


# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
from termcolor import cprint, colored


class Man:

    def __init__(self, name):
        self.fullness = 50
        self.name = name.title()
        self.house = None

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
        self.house.money += 50
        self.fullness -= 10

    def watch_MTV(self):
        cprint(f'{self.name} смотрел MTV', color='blue')
        self.fullness -= 10

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

    def act(self):
        if self.fullness <= 0:
            cprint(f'{self.name} умер от голода', color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:
    def __init__(self):
        self.food = 10
        self.money = 50

    def __str__(self):
        return colored(f'В доме осталось {self.food} еды и {self.money} денег', color='green')


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни')
    ]
my_sweet_home = House()
for citizen in citizens:
    citizen.go_into_the_house(my_sweet_home)
for day in range(1, 366):
    cprint(f'============= День {day} =============', color='yellow')
    for citizen in citizens:
        citizen.act()
    print('------------- В конце дня -------------')
    for citizen in citizens:
        print(citizen)

    print(my_sweet_home)
# Создадим двух людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должн быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.
