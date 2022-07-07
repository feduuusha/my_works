# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

class NotNameError(Exception):

    def __init__(self, message='Поле имени содержит НЕ только буквы'):
        self.message = message
        super().__init__(self.message)


class NotEmailError(Exception):

    def __init__(self, message='поле емейл НЕ содержит @ и .(точку)'):
        self.message = message
        super().__init__(self.message)


def verify_name(name):
    for char in name:
        if char.isalpha():
            continue
        else:
            raise NotNameError()


def verify_email(email):
    if '@' in email and '.' in email:
        pass
    else:
        raise NotEmailError()


def verify_age(age):
    if age > 99 or age < 10:
        raise ValueError('Не соответсвует возраст')


with open('registrations.txt', 'r', encoding='utf8') as file:
    for line in file:
        try:
            name, email, age = line.split(' ')
            age = int(age)
            verify_name(name)
            verify_email(email)
            verify_age(age)
        except (ValueError, NotNameError, NotEmailError) as exc:
            with open('registrations_bad.log', 'a', encoding='utf8') as f_log:
                f_log.write(f"{line.rstrip()} {exc} \n")
        else:
            with open('registrations_good.log', 'a', encoding='utf8') as f_log:
                f_log.write(line)
