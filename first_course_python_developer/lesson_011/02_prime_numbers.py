# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n+1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, n):
        self.n = n
        self.counter = 0
        self.prime_numbers = []
        self.get_prime_numbers()

    def get_prime_numbers(self):
        for number in range(2, self.n+1):
            for prime in self.prime_numbers:
                if number % prime == 0:
                    break
            else:
                self.prime_numbers.append(number)

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        self.counter += 1
        if self.counter <= len(self.prime_numbers):
            return self.prime_numbers[self.counter - 1]
        raise StopIteration()


prime_number_iterator = PrimeNumbers(n=10000)
for number in prime_number_iterator:
    print(number)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


for number in prime_numbers_generator(n=10000):
    print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
def lucky_number(n):
    n = str(n)
    length = len(n) // 2
    start = n[:length]
    total_start = 0
    total_end = 0
    if len(n) % 2 == 0:
        end = n[length:]
    else:
        end = n[length + 1:]
    for char in start:
        total_start += int(char)
    for char in end:
        total_end += int(char)
    if total_start == total_end and len(n) > 1:
        return True
    else:
        return False


for number in prime_numbers_generator(n=10000):
    if lucky_number(number):
        print(number)


# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
def palindrom(n):
    n = str(n)
    length = len(n) // 2
    start = n[:length]
    if len(n) % 2 == 0:
        end = n[length:]
    else:
        end = n[length + 1:]
    if start == end[::-1]:
        return True
    else:
        return False


for number in prime_numbers_generator(n=10000):
    if palindrom(number):
        print(number)

# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
for number in prime_numbers_generator(n=10000):
    if palindrom(number) and lucky_number(number):
        print(number)
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
