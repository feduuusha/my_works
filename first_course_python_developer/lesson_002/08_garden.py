#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)
my_set = garden_set & meadow_set
print(my_set)

# выведите на консоль все виды цветов
all_flowers = garden_set | meadow_set
print(all_flowers)
# выведите на консоль те, которые растут и там и там
print(my_set)

# выведите на консоль те, которые растут в саду, но не растут на лугу
only_garden = garden_set - meadow_set
print(only_garden)

# выведите на консоль те, которые растут на лугу, но не растут в саду
only_meadow = meadow_set - garden_set
print(only_meadow)
