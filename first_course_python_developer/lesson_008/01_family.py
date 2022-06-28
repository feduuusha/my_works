# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


#                                        Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    all_money = 100

    def __init__(self):
        self.money = 100
        self.eat = 50
        self.dirt = 0
        self.cat_eat = 30

    def __str__(self):
        return f'В доме {self.money} денег, {self.eat} еды, {self.dirt} грязи и {self.cat_eat} кошачьей еды'


class Human:
    all_eat = 0

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = None

    def __str__(self):
        return f'{self.name} сыт на {self.fullness}, счастлив на {self.happiness} '

    def go_to_house(self, house_name):
        self.house = house_name
        print(f'{self.name} заехал. {house_name}')

    def petting_the_cat(self):
        self.happiness += 5
        print(f'{self.name} погладил кота')


class Husband(Human):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        dice = randint(1, 3)
        if self.fullness <= 0 or self.happiness < 10:
            cprint(f'{self.name} умер...', color='red')
        if self.fullness <= 20:
            self.eat()
        elif self.house.money <= 50:
            self.work()
        elif self.happiness <= 10:
            self.gaming()
        else:
            if dice == 1:
                self.gaming()
            elif dice == 2:
                self.work()
            elif dice == 3:
                self.petting_the_cat()
        self.house.dirt += 5
        if self.house.dirt >= 90:
            self.happiness -= 10

    def eat(self):
        if self.house.eat >= 30:
            self.fullness += 30
            Human.all_eat += 30
            self.house.eat -= 30
            print(f'{self.name} покушал')
        else:
            self.fullness += self.house.eat
            Human.all_eat += self.house.eat
            self.house.eat -= self.house.eat
            print(f'{self.name} покушал')

    def work(self):
        House.all_money += 150
        self.house.money += 150
        self.fullness -= 10
        print(f'{self.name} сходил на работу')

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20
        print(f'{self.name} поиграл в танки')


class Wife(Human):
    all_coat = 0

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        dice = randint(1, 3)
        if self.fullness <= 0 or self.happiness < 10:
            cprint(f'{self.name} умер...', color='red')
        if self.fullness <= 20:
            self.eat()
        elif self.house.eat <= 50:
            self.shopping()
        elif self.house.cat_eat <= 50:
            self.cat_shopping()
        elif self.happiness <= 20:
            self.buy_fur_coat()
        elif self.house.dirt >= 80:
            self.clean_house()
        else:
            if dice == 1:
                self.shopping()
            elif dice == 2:
                self.clean_house()
            elif dice == 3:
                self.petting_the_cat()
        if self.house.dirt >= 90:
            self.happiness -= 10

    def eat(self):
        if self.house.eat >= 30:
            self.fullness += 30
            Human.all_eat += 30
            self.house.eat -= 30
            print(f'{self.name} покушала')
        else:
            self.fullness += self.house.eat
            Human.all_eat += self.house.eat
            self.house.eat -= self.house.eat
            print(f'{self.name} покушала')

    def shopping(self):
        if self.house.money >= 50:
            self.house.money -= 50
            self.house.eat += 50
            print(f'{self.name} купила еды')
        else:
            cprint(f'Нехватает денег на еду...', color='red')

    def cat_shopping(self):
        if self.house.money >= 50:
            self.house.money -= 50
            self.house.cat_eat += 50
            print(f'{self.name} купила еды кошке')
        else:
            cprint(f'Нехватает денег на еду для кошки...', color='red')

    def buy_fur_coat(self):
        if self.house.money >= 350:
            self.house.money -= 350
            self.happiness += 60
            self.fullness -= 10
            Wife.all_eat += 1
            print(f'{self.name} купила шубу')
        else:
            cprint(f'Нехватает денег на шубу', color='red')

    def clean_house(self):
        if self.house.dirt < 100:
            self.house.dirt -= self.house.dirt
            self.fullness -= 10
            print(f'{self.name} убрала дом')
        else:
            self.house.dirt -= 100
            self.fullness -= 10
            print(f'{self.name} убрала дом')


# Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.house = None

    def __str__(self):
        return f'{self.name} сыта на {self.fullness}'

    def act(self):
        dice = randint(1, 2)
        if self.fullness <= 0:
            cprint(f'{self.name} умер...', color='red')
        else:
            if self.fullness <= 20:
                self.eat()
            elif dice == 1:
                self.soil()
            elif dice == 2:
                self.sleep()

    def go_to_house(self, house_name):
        self.house = house_name

    def eat(self):
        if self.house.cat_eat >= 10:
            self.fullness += 20
            self.house.cat_eat -= 10
            print(f'{self.name} поел')
        else:
            if self.house.cat_eat:
                self.fullness += 2 * self.house.cat_eat
                self.house.cat_eat -= self.house.cat_eat
                print(f'{self.name} поел')
            else:
                cprint('В доме нет еды для кота', color='red')

    def sleep(self):
        self.fullness -= 10
        print(f'{self.name} проспал весь день')

    def soil(self):
        self.house.dirt += 5
        self.fullness -= 10
        print(f'{self.name} подрал обои')


# Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья - не меняется, всегда ==100 ;)

class Child(Human):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness <= 20:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        self.fullness += 10
        self.house.eat -= 10
        print(f'{self.name} поел')

    def sleep(self):
        self.fullness -= 10
        print(f'{self.name} весь день проспал')


# Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')
serge.go_to_house(home)
masha.go_to_house(home)
kolya.go_to_house(home)
murzik.go_to_house(home)

for day in range(1, 366):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(str(serge), color='cyan')
    cprint(str(masha), color='cyan')
    cprint(str(kolya), color='cyan')
    cprint(str(murzik), color='cyan')
    cprint(str(home), color='cyan')

cprint(f'Всего потрачено денег - {House.all_money}')
cprint(f'Всего съедено еды - {Human.all_eat}')
cprint(f'Всего куплено шуб - {Wife.all_coat}')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
