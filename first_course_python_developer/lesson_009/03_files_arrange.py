# -*- coding: utf-8 -*-

import os,time
import datetime
import shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import zipfile

file_name = 'icons.zip'
with zipfile.ZipFile(file_name, 'r') as zfile:
    fail_list = [text_file.filename for text_file in zfile.infolist() if text_file.filename.endswith('.png')]
    for file in fail_list:
        zfile.extract(file)


def restore_timestamps_of_zip_contents(zipname, extract_dir):
    for f in zipfile.ZipFile(zipname, 'r').infolist():
        fullpath = os.path.join(extract_dir, f.filename)
        date_time = time.mktime(f.date_time + (0, 0, -1))
        os.utime(os.path.normpath(fullpath), (date_time, date_time))


restore_timestamps_of_zip_contents('icons.zip', 'my_icons')

my_list = ['C:\\Users\\vorop\\PycharmProjects\\my_works\\'
           'first_course_python_developer\\lesson_009\\my_icons\\icons\\actions',
           'C:\\Users\\vorop\\PycharmProjects\\my_works\\'
           'first_course_python_developer\\lesson_009\\my_icons\\icons\\animations',
           'C:\\Users\\vorop\\PycharmProjects\\my_works\\'
           'first_course_python_developer\\lesson_009\\my_icons\\icons\\apps',
           'C:\\Users\\vorop\\PycharmProjects\\my_works\\'
           'first_course_python_developer\\lesson_009\\my_icons\\icons\\categories',
           'C:\\Users\\vorop\\PycharmProjects\\my_works\\'
           'first_course_python_developer\\lesson_009\\my_icons\\icons\\devices',
           'C:\\Users\\vorop\\PycharmProjects\\my_works\\'
           'first_course_python_developer\\lesson_009\\my_icons\\icons\\emblems',
           'C:\\Users\\vorop\\PycharmProjects\\my_works\\'
           'first_course_python_developer\\lesson_009\\my_icons\\icons\\emotes',
           'C:\\Users\\vorop\\PycharmProjects\\my_works\\'
           'first_course_python_developer\\lesson_009\\my_icons\\icons\\mimetypes',
           'C:\\Users\\vorop\\PycharmProjects\\my_works\\'
           'first_course_python_developer\\lesson_009\\my_icons\\icons\\places',
           'C:\\Users\\vorop\\PycharmProjects\\my_works\\'
           'first_course_python_developer\\lesson_009\\my_icons\\icons\\status']
for p in my_list:
    os.chdir(p)


    def d():
        for x in range(1, 13):
            if x > 9:
                if not os.path.exists(f'{x}'):
                    os.makedirs(f'{x}')
            else:
                if not os.path.exists(f'0{x}'):
                    os.makedirs(f'0{x}')


    def mod_date(file):
        t = os.path.getmtime(file)
        return datetime.datetime.fromtimestamp(t)

    a = []
    for root, dirs, files in os.walk(p):
        for file in files:
            if file[-3:] not in a:
                a.append(file[-3:])
            if file[-3:] in a:
                year = str(mod_date(file))[:10][:4]
                if not os.path.exists(year):
                    os.makedirs(year)
                os.chdir(p+'/'+year)
                d()
                os.chdir(p)

    try:
        for root, dirs, files in os.walk(p):
            for file in files:
                if file[-3:] in a:
                    year = str(mod_date(file))[:10][:4]
                    month = str(mod_date(file))[:10][5:7]
                    shutil.move(file, year+'/'+month+'/'+file)
    except EnvironmentError:
        'Вроде готово'
# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
