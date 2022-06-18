from random import choice


_number_to_check = ''
_number = ''


def make_a_number():
    global _number
    _number = ''
    numbers = '0123456789'
    numbers_without_0 = '123456789'
    for i in range(4):
        if i == 0:
            z = choice(numbers_without_0)
            _number += z
            numbers = numbers.replace(_number[i], '', 1)
        else:
            z = choice(numbers)
            _number += z
            numbers = numbers.replace(_number[i], '', 1)


def check_the_number(number_to_check):
    global _number_to_check
    for i in number_to_check:
        if number_to_check.count(i) == 1:
            continue
        else:
            return False
    if len(number_to_check) == 4 and type(number_to_check) == str:
        j = 0
        z = 0
        my_dict = {}
        _new_number = ''
        _number_to_check = number_to_check
        for i, k in enumerate(number_to_check):
            if k in _number and i == _number.index(k):
                _number.replace(k, '')
                j += 1
            if k in _number and i != _number.index(k):
                _number.replace(k, '')
                z += 1
        my_dict['Быки'] = j
        my_dict['Коровы'] = z
        if my_dict:
            return my_dict
    else:
        return False


def is_game_end():
    if _number == _number_to_check:
        return True
    else:
        return False
