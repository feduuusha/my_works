# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код

class Water:
    def __init__(self):
        self.name = 'Вода'

    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if other.name == 'Воздух':
            return Storm()
        elif other.name == 'Огонь':
            return Steam()
        elif other.name == 'Земля':
            return Dirt()
        elif other.name == 'Пар':
            return Ethanol()
        elif other.name == 'Спирт':
            return Vodka()
        else:
            return None


class Air:
    def __init__(self):
        self.name = 'Воздух'

    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if other.name == 'Огонь':
            return Lightning()
        elif other.name == 'Земля':
            return Dust()
        elif other.name == 'Вода':
            return Storm()
        elif other.name == 'Спирт':
            return Water()
        else:
            return None


class Fire:
    def __init__(self):
        self.name = 'Огонь'

    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if other.name == 'Земля':
            return Lava()
        elif other.name == 'Вода':
            return Steam()
        elif other.name == 'Воздух':
            return Lightning()
        elif other.name == 'Спирт':
            return Boom()
        else:
            return None


class Earth:
    def __init__(self):
        self.name = 'Земля'

    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if other.name == 'Вода':
            return Dirt()
        elif other.name == 'Воздух':
            return Dust()
        elif other.name == 'Огонь':
            return Lava()
        else:
            return None


class Storm:
    def __init__(self):
        self.name = 'Шторм'

    def __str__(self):
        return 'Шторм'

    def __add__(self, other):
        return None


class Steam:
    def __init__(self):
        self.name = "Пар"

    def __str__(self):
        return 'Пар'

    def __add__(self, other):
        return None


class Dirt:
    def __init__(self):
        self.name = 'Грязь'

    def __str__(self):
        return 'Грязь'

    def __add__(self, other):
        return None


class Lightning:
    def __init__(self):
        self.name = 'Молния'

    def __str__(self):
        return 'Молния'

    def __add__(self, other):
        return None


class Dust:
    def __init__(self):
        self.name = 'Пыль'

    def __str__(self):
        return 'Пыль'

    def __add__(self, other):
        return None


class Lava:
    def __init__(self):
        self.name = 'Лава'

    def __str__(self):
        return 'Лава'

    def __add__(self, other):
        return None


class Ethanol:
    def __init__(self):
        self.name = 'Спирт'

    def __str__(self):
        return 'Спирт'

    def __add__(self, other):
        if other.name == 'Огонь':
            return Boom()
        elif other.name == 'Вода':
            return Vodka()
        elif other.name == 'Воздух':
            return Water()
        else:
            return None


class Boom:
    def __init__(self):
        self.name = 'Взрыв'

    def __str__(self):
        return 'Взрыв'

    def __add__(self, other):
        return None


class Vodka:
    def __init__(self):
        self.name = 'Водка'

    def __str__(self):
        return 'Водка'

    def __add__(self, other):
        return None


print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())
print(Storm(), '+', Air(), '=', Storm() + Air())
print(Water() + Fire())
print(Water() + Earth())
print(Air() + Earth())
print(Air() + Fire())
print(Fire() + Earth())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Добавим в игру элемент Спирт
# Спирт будет получаться за счет смешения Воды и Пара
# Спирт + Вода = Водка
print(Ethanol() + Water())
# Спирт + Огонь = Взрыв
print(Ethanol() + Fire())
# Спирт + Воздух = Вода
print(Ethanol() + Air())
# Придумать что будет при сложении существующих элементов с новым.
print(Water() + (Water() + Fire()))
