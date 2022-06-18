# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
number_of_months = {'Январь': 1, 'Февраль': 2, 'Март': 3, 'Апрель': 4, 'Май': 5, 'Июнь': 6,
                    'Июль': 7, 'Август': 8, 'Сентябрь': 9, 'Октябрь': 10, 'Ноябрь': 11, 'Декабрь': 12}
months = {'Январь': 31, 'Февраль': 28, 'Март': 31, 'Апрель': 30, 'Май': 31, 'Июнь': 30,
          'Июль': 31, 'Август': 31, 'Сентябрь': 30, 'Октябрь': 31, 'Ноябрь': 30, 'Декабрь': 31}
name_of_months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
                  'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
user_input = input("Введите, пожалуйста, номер месяца: ")
number = int(user_input)
print('Вы ввели', number)
if number <= len(number_of_months):
    print('Это месяц под названием - ', name_of_months[number-1])
if number == number_of_months['Январь']:
    print('В ', number, 'месяце', months['Январь'], 'дней')
elif number == number_of_months['Февраль']:
    print('В ', number, 'месяце', months['Февраль'], 'дней')
elif number == number_of_months['Март']:
    print('В ', number, 'месяце', months['Март'], 'дней')
elif number == number_of_months['Апрель']:
    print('В ', number, 'месяце', months['Апрель'], 'дней')
elif number == number_of_months['Май']:
    print('В ', number, 'месяце', months['Май'], 'дней')
elif number == number_of_months['Июнь']:
    print('В ', number, 'месяце', months['Июнь'], 'дней')
elif number == number_of_months['Июль']:
    print('В ', number, 'месяце', months['Июль'], 'дней')
elif number == number_of_months['Август']:
    print('В ', number, 'месяце', months['Август'], 'дней')
elif number == number_of_months['Сентябрь']:
    print('В ', number, 'месяце', months['Сентябрь'], 'дней')
elif number == number_of_months['Октябрь']:
    print('В ', number, 'месяце', months['Октябрь'], 'дней')
elif number == number_of_months['Ноябрь']:
    print('В ', number, 'месяце', months['Ноябрь'], 'дней')
elif number == number_of_months['Декабрь']:
    print('В ', number, 'месяце', months['Декабрь'], 'дней')
else:
    print('Вы неправильно ввели месяц, попробуйте заного :(')
