#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

moscow = sites['Moscow']
paris = sites['Paris']
london = sites['London']
moscow_london = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** 0.5
moscow_paris = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** 0.5
paris_london = ((paris[0] - london[0]) ** 2 + (paris[1] - london[1]) ** 2) ** 0.5
distances = {'Расстояние от Москвы до Лондона': moscow_london, 'Расстояние от Москвы до Парижа': moscow_paris,
             'Расстояние от Парижа до Лондона': paris_london, 'Расстояние от Парижа до Москвы': moscow_paris,
             'Расстояние от Лондона до Москвы': moscow_london, 'Расстояние от Лондона до Парижа': paris_london}

pprint(distances)
