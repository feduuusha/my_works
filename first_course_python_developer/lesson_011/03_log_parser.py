# -*- coding: utf-8 -*-
from collections import defaultdict

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


def log_parser(file):
    counter = 0
    with open(file, 'r') as f_obj:
        logs = defaultdict(int)
        for line in f_obj:
            time, status = line[:-1].split('] ')
            if status == 'NOK':
                logs[time[1:17]] += 1
        logs = [(x, logs[x]) for x in logs.keys()]
    for _ in range(len(logs)):
        yield logs[counter]
        counter += 1


grouped_events = log_parser('events.txt')
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
