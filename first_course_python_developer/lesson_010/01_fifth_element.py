# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42
try:
    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
except (ValueError, IndexError, Exception) as exc:
    if type(exc) == ValueError:
        print(f'Невозможно преобразовать к числу: {exc}')
    elif type(exc) == IndexError:
        print(f'Неправильный размер строки: {exc}')
    else:
        print('Вы что-то сделали не так :(')
else:
    print(f"- Leeloo Dallas! Multi-pass № {result}!")

# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение
