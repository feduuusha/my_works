from random import randint

MAX_BUNCHES = 5
MAX_BUNCHES_SIZE = 20

_holder = {}


def put_stones():
    global _holder
    _holder = {}
    for i in range(1, MAX_BUNCHES + 1):
        _holder[i] = randint(1, MAX_BUNCHES_SIZE)


def put_from_bunch(position, quantity):
    if position in _holder:
        _holder[position] -= quantity
        return True
    else:
        return False


def stones_positions():
    res = []
    for key in sorted(_holder.keys()):
        res.append(_holder[key])
    return res


def is_end_game():
    return sum(_holder.values()) == 0
