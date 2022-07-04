# -*- coding: utf-8 -*-
import os.path
import zipfile

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class LetterStatistics:

    def __init__(self, file_name, sort_by_value=None, sort_by_key=None):
        self.file_name = file_name
        self.stat = {}
        self.all_chars = 0
        self.sort_by_value = sort_by_value
        self.sort_by_key = sort_by_key

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect_stat(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r') as file:
            for stroke in file:
                for char in stroke:
                    if char.isalpha():
                        if char in self.stat:
                            self.stat[char] += 1
                        else:
                            self.stat[char] = 1

    def sort_stat(self):
        if self.sort_by_value is not None:
            sorted_tuple = sorted(self.stat.items(), key=lambda x: x[1], reverse=not self.sort_by_value)
            self.stat = dict(sorted_tuple)
        if self.sort_by_key is not None:
            sorted_keys = sorted(self.stat.items(), key=lambda x: x[0], reverse=not self.sort_by_key)
            self.stat = dict(sorted_keys)

    def formatting(self):
        print('+---------+---------+')
        print('|  буква  | частота |')
        print('+---------+---------+')
        for char, count in self.stat.items():
            print(f'|{char:^9}|{count:8d} |')
        for i in self.stat.values():
            self.all_chars += i
        print('+---------+---------+')
        print(f'|  итого  |{self.all_chars:8d} |')
        print('+---------+---------+')


my_file = os.path.normpath("C:\\Users\\vorop\\PycharmProjects\\"
                           "my_works\\first_course_python_developer\\"
                           "lesson_009\\python_snippets\\voyna-i-mir.txt.zip")
stat = LetterStatistics(file_name=my_file,  sort_by_key=True)
stat.collect_stat()
stat.sort_stat()
stat.formatting()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
