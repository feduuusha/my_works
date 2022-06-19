# -*- coding: utf-8 -*-

import my_burger
from pprint import pprint

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.
# Два рубленых бифштекса из натуральной цельной говядины с двумя кусочками сыра Чеддер на карамелизованной булочке,
# заправленной горчицей, кетчупом, луком и двумя кусочками маринованного огурчика
my_burger.add_bun()
my_burger.add_cucumber()
my_burger.add_tomato()
my_burger.add_cucumber()
my_burger.add_mayonnaise()
my_burger.add_cheese()
my_burger.add_chop()
my_burger.add_cheese()
my_burger.add_chop()
my_burger.add_bun()
burger = [my_burger.add_bun(),
          my_burger.add_cucumber(),
          my_burger.add_tomato(),
          my_burger.add_cucumber(),
          my_burger.add_mayonnaise(),
          my_burger.add_cheese(),
          my_burger.add_chop(),
          my_burger.add_cheese(),
          my_burger.add_chop(),
          my_burger.add_bun()]
print('А теперь что у нас получилось')
pprint(burger)
# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger
# Чикен примьер
# Сочная куриная котлета в хрустящей панировке, сыр Чеддер, ароматный бекон, ломтик помидора,
# свежий салат, специальный соус и булочка с кунжутом
my_burger.add_bun()
my_burger.add_cucumber()
my_burger.add_tomato()
my_burger.add_cucumber()
my_burger.add_special_sous()
my_burger.add_bacon()
my_burger.add_chicken_cutlet()
my_burger.add_cheese()
my_burger.add_special_sous()
my_burger.add_bun()
chicken_premier = [my_burger.add_bun(),
                   my_burger.add_cucumber(),
                   my_burger.add_tomato(),
                   my_burger.add_cucumber(),
                   my_burger.add_special_sous(),
                   my_burger.add_bacon(),
                   my_burger.add_chicken_cutlet(),
                   my_burger.add_cheese(),
                   my_burger.add_special_sous(),
                   my_burger.add_bun()]
print('А вот что получилось:')
pprint(chicken_premier)
