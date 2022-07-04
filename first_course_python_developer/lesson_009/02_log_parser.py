# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class LogStatistics:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.group_stats = {}

    def collect_stat(self):
        with open(self.file_name, 'r') as file:
            for line in file:
                status = line[-4:-1]
                my_line = line[1:17]
                if status == 'NOK':
                    if my_line in self.stat:
                        self.stat[my_line] += 1
                    else:
                        self.stat[my_line] = 1

    def group_stat(self, group_stat_for):
        """ Группировка статистики может быть по году, месяцу, часу
            Для этого использовать параметр group_stat_for значениями которого могут быть:
            Year - по году
            Month - по месяцу
            Hour - по часу
        """
        if group_stat_for == 'Month':
            for key in self.stat.keys():
                if key[:7] in self.group_stats:
                    self.group_stats[key[:7]] += self.stat[key]
                else:
                    self.group_stats[key[:7]] = self.stat[key]
        elif group_stat_for == 'Year':
            for key in self.stat.keys():
                if key[:4] in self.group_stats:
                    self.group_stats[key[:4]] += self.stat[key]
                else:
                    self.group_stats[key[:4]] = self.stat[key]
        elif group_stat_for == 'Hour':
            for key in self.stat.keys():
                if f'{key[:14]}00' in self.group_stats:
                    self.group_stats[f'{key[:14]}00'] += self.stat[key]
                else:
                    self.group_stats[f'{key[:14]}00'] = self.stat[key]
        self.stat = self.group_stats

    def write_stat(self, file_name_to_write):
        with open(file_name_to_write, 'w') as file:
            for key in self.stat.keys():
                file.write(f'[{key}] {self.stat[key]}')
                file.write('\n')


my_file = LogStatistics(file_name='events.txt')
my_file.collect_stat()
my_file.write_stat(file_name_to_write='out.txt')
my_file.group_stat(group_stat_for='Hour')
my_file.write_stat(file_name_to_write='out.txt')

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
