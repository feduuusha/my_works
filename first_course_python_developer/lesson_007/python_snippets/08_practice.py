# -*- coding: utf-8 -*-

from random import randint


# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.fullness = 50
        self.food = 50
        self.money = 0
        self.name = name.title()

    def __str__(self):
        return f'Я - {self.name}, я сыт на {self.fullness}%, у меня {self.food} еды и {self.money} денег '

    def eat(self):
        if self.food >= 10:
            print(f'{self.name} поел')
            self.fullness += 10
            self.food -= 10
        else:
            print(f'У {self.name} нет еды (')

    def work(self):
        print(f'{self.name} сходил на работу')
        self.money += 50
        self.fullness -= 10

    def play_dota(self):
        cprint(f'{self.name} поиграл в доту', color='green')
        self.fullness -= 10

    def shopping(self):
        if self.money >= 50:
            print(f'{self.name} сходил в магазин за едой')
            self.money -= 50
            self.food += 50
        else:
            print(f'У {self.name} кончились деньги')

    def act(self):
        if self.fullness <= 0:
            print(f'{self.name} умер от голода')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.food < 10:
            self.shopping()
        elif self.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play_dota()


vasya = Man('Вася')
for day in range(1, 366):
    cprint(f'============= День{day} =============', color='yellow')
    vasya.act()
    print(vasya)
# Создадим двух людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должн быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.
