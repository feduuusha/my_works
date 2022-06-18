#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца


# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.
first_film = my_favorite_movies[0:10]
last_film = my_favorite_movies[42:]
second_film = my_favorite_movies[12:24]
fourth_film = my_favorite_movies[-22:-17]
print(first_film, last_film, second_film, fourth_film)
