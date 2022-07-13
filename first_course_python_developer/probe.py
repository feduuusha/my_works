# from pprint import pprint
# from statistics import mean
#
#
# extract_of_ratings = {'Биология': [4, 5, 4, 4],
#                       'География': [3, 4, 5, 5, 4],
#                       'Информатика': [4, 4, 5, 5, 5, 5, 5, 4, 5, 5, 5, 2, 5, 5, 5, 4, 5, 4, 5, 4, 4, 5, 5],
#                       'История': [4, 4, 3, 5, 4, 4, 4],
#                       'Литература': [5, 4, 5, 4, 5, 4, 5, 5],
#                       'Математика': [4, 4, 4, 5, 5, 5, 4, 5, 4, 4, 5, 5, 4, 5,
#                                      5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5],
#                       'Обществознание': [4, 4, 4, 5, 4, 5, 5, 5],
#                       'Русский язык': [5, 4, 5, 5, 5, 4, 4],
#                       'Физика': [4, 2, 3, 4, 5, 4, 2, 5, 4, 4, 5, 5, 4, 3, 4],
#                       'Физическая культура': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 4, 4, 4, 5, 4, 5, 5, 5, 5, 5],
#                       'Химия': [4, 4, 4, 5],
#                       'Индивидуальный проект': [5, 4, 5, 5, 5],
#                       'Иностранный язык (английский)': [4, 5, 5, 5, 4, 5, 5, 4, 5, 5, 4, 5, 5, 4, 5, 5, 4, 4],
#                       'Основы безопасности жизнедеятельности': [5, 5, 4, 5, 5, 5, 5, 5, 4],
#                       'Родной язык (русский)': [4, 5, 4, 5],
#                       'Уравнения и неравенства с параметрами': [5, 5, 5, 5, 5]}
# biology_avg = mean(extract_of_ratings['Биология'])
# geography_avg = mean(extract_of_ratings['География'])
# pprint((biology_avg, geography_avg))


# def max_digit(number: int) -> int:
#     number_str = str(number)
#     if len(number_str) == 1:
#         return number
#     else:
#         number_str = str(number)
#         list_of_numbers = []
#         for i in number_str:
#             list_of_numbers.append(i)
#         return int(max(list_of_numbers))
# print(max_digit(202139010293))


# spisok = []
# for i in range(8812, 12286):
#     if i % 19 == 0:
#         if i % 4 != 0:
#             if i % 9 != 0:
#                 if i % 14 != 0:
#                     spisok.append(i)
# print(len(spisok), max(spisok))


# def end_zeros(num: int) -> int:
#     num_str = str(num)
#     k = 0
#     for i in num_str[::-1]:
#         if i == '0':
#             k += 1
#         else:
#             return k
#     return k
#
# print(end_zeros(100100))


# letters = 'ЭТАН'
# k = 0
# for a in letters:
#     for b in letters:
#         for c in letters:
#             for d in letters:
#                 word = a + b + c + d
#                 if word.count('Э' or 'А') == 1:
#                     k += 1
# print(k)


# from typing import Iterable
#
#
# def remove_all_before(items: list, border: int) -> Iterable:
#     items_remove = []
#     if border in items:
#         for i in items:
#             if i == border:
#                 for k in items_remove:
#                     items.remove(k)
#             elif items.index(i) > items.index(border):
#                 break
#             else:
#                 items_remove.append(i)
#     return items
#
#
# print(remove_all_before([1, 1, 2, 2, 3, 4, 5], 2))


# # РИСОВАНИЕ СЕРДЕЧКА С ТЕКСТОМ
# # Import turtle package
# import turtle
# import time
#
# # Creating a turtle object(pen)
# pen = turtle.Turtle()
#
#
# # Defining a method to draw curve
# def curve():
#     for i in range(200):
#         # Defining step by step curve motion
#         pen.right(1)
#         pen.forward(1)
#
#
# # Defining method to draw a full heart
# def heart():
#     # Set the fill color to red
#     pen.fillcolor('red')
#
#     # Start filling the color
#     pen.begin_fill()
#
#     # Draw the left line
#     pen.left(140)
#     pen.forward(113)
#
#     # Draw the left curve
#     curve()
#     pen.left(120)
#
#     # Draw the right curve
#     curve()
#
#     # Draw the right line
#     pen.forward(112)
#
#     # Ending the filling of the color
#     pen.end_fill()
#
#
# # Defining method to write text
# def txt():
#     # Move turtle to air
#     pen.up()
#
#     # Move turtle to a given position
#     pen.setpos(-68, 95)
#
#     # Move the turtle to the ground
#     pen.down()
#
#     # Set the text color to lightgreen
#     pen.color('lightgreen')
#
#     # Write the specified text in
#     # specified font style and size
#     pen.write("I love Mama", font=(
#         "Times New Roman", 18, "bold"))
#     time.sleep(5)
#
#
# # Draw a heart
# heart()
#
# pen.ht()
# # Write text
# txt()
#
# # To hide turtle
# pen.ht()


# # Функция которая рисует пузырёк
# import turtle
# import time
#
#
# def draw_bubble(drawing_point_x, drawing_point_y, step, radius):
#     pen = turtle.Turtle()
#     pen.up()
#     pen.setpos(drawing_point_x, drawing_point_y)
#     pen.down()
#     pen.circle(radius)
#     pen.up()
#     pen.setpos(drawing_point_x, drawing_point_y + step)
#     pen.down()
#     pen.circle(radius - step)
#     pen.up()
#     pen.setpos(drawing_point_x, drawing_point_y + 2 * step)
#     pen.down()
#     pen.circle(radius - 2 * step)
#     pen.up()
#     pen.setpos(drawing_point_x, drawing_point_y + 3 * step)
#     pen.down()
#     pen.circle(radius - 3 * step)
#     time.sleep(2)
#
#
# draw_bubble(20, 20, 10, 200)


# def correct_sentence(text: str) -> str:
#     first_word = text[0]
#     if text.endswith('.'):
#         return text.replace(first_word, first_word.capitalize(), 1)
#     else:
#         return text.replace(first_word, first_word.capitalize(), 1) + '.'
#
#
# print(correct_sentence('welcome to New York'))


# def is_all_upper(text: str):
#     stroke = []
#     if len(text) != 0:
#         for i in text:
#             if i.isupper():
#                 stroke.append(i)
#             elif i.isspace():
#                 stroke.append(i)
#             elif i.isnumeric():
#                 stroke.append(i)
#     if ''.join(stroke) == text:
#             return True
#         else:
#             return False
#     else:
#         return True
#
#
# print(is_all_upper('55'))


# def replace_first(items: list):
#     if len(items) < 2:
#         return items
#     else:
#         items.append(items[0])
#         items.remove(items[0])
#         return items
#
#
# print(replace_first([1, 2, 4, 5, 6]))


# def beginning_zeros(number: str) -> int:
#     k = 0
#     if number[0] != '0':
#         return 0
#     else:
#         for i in number:
#             if i == '0':
#                 k += 1
#             else:
#                 break
#         return k
#
#
# beginning_zeros('002')


# for n in range(61, 100):
#     s = '1' * n
#     while '111' in s:
#         s = s.replace('111', '2', 1)
#         s = s.replace('222', '11', 1)
#     if s == '221':
#         print(n)
#         break


# def between_markers(text: str, begin: str, end: str) -> str:
#     start = 0
#     for i, k in enumerate(text):
#         if k == begin:
#             start = i + 1
#         elif k == end:
#             end = i
#     return text[start:end]
#
#
# print(between_markers('Котик <хочет> кушать', '<', '>'))


# def nearest_value(values: set, one: int) -> int:
#     if one in values:
#         return one
#     else:
#         values.add(one)
#         values = sorted(values)
#         if len(values) > 3 and values.index(one) != 0 and values.index(one) != len(values) - 1:
#             new_values = values[values.index(one) - 1: values.index(one) + 2]
#             if one - new_values[0] > new_values[2] - one:
#                 return new_values[2]
#             else:
#                 return new_values[0]
#         else:
#             if max(values) == one:
#                 return values[values.index(one) - 1]
#             elif min(values) == one:
#                 return values[values.index(one) + 1]
#             else:
#                 return min(values)
#
#
# my_set = {1, 2, 3, 5, 7, 5, 4, 6}
# print(nearest_value({0, -2}, -1))


# def split_pairs(a: str):
#     my_list = []
#     n = 2
#     if len(a) % 2 == 0:
#         for i in range(0, len(a), n):
#             my_list.append(a[i:i+n])
#         return my_list
#     else:
#         a.replace(a[-1], '', 1)
#         for i in range(0, len(a), n):
#             my_list.append(a[i:i + n])
#         my_list.remove(my_list[-1])
#         my_list.append(a[-1] + '_')
#         return my_list
#
#
# print(split_pairs('adsadasdad'))


# def sum_numbers(text: str) -> int:
#     z = 0
#     stroke = ''
#     for k, i in enumerate(text):
#         if k == len(text) - 1:
#             if i.isnumeric():
#                 stroke += i
#                 z += int(stroke)
#                 return z
#         if i.isnumeric() and not(text[k+1].isalpha()):
#             stroke += i
#         if i.isspace() and stroke != '':
#             z += int(stroke)
#             stroke = ''
#     return z
#
#
# print(sum_numbers('my numbers is 2'))


# def checkio(words: str) -> bool:
#     word = ''
#     number = ''
#     list_of_words = []
#     words += ' '
#     for i in words:
#         if i.isalpha():
#             word += i
#         elif i.isnumeric():
#             number += i
#         elif i.isspace() or words.index(i) + 1 == len(words):
#             if len(word) > 0:
#                 list_of_words.append(word)
#                 word = ''
#             elif len(number) > 0:
#                 list_of_words.append(number)
#                 number = ''
#     k = 0
#     list_of_words.append(' ')
#     for z in list_of_words:
#         if k > 2:
#             return True
#         elif z.isalpha():
#             k += 1
#         elif z.isnumeric():
#             k = 0
#         else:
#             return False
#
#
#
# print(checkio("Hi"))


# def checkio(array: list) -> int:
#     """
#         sums even-indexes elements and multiply at the last
#     """
#     sum = 0
#     if len(array) == 0:
#         return 0
#     for i in range(0, len(array), 2):
#         sum += array[i]
#     multiply = sum * array[-1]
#     return multiply
#
#
# print(checkio([]))


# def checkio(data: list) -> list:
#     new_data = []
#     for i in data:
#         if data.count(i) > 1:
#             new_data.append(i)
#     return new_data
#
#
# print(checkio([5, 5, 5, 5, 5]))


# def count_digits(text: str) -> int:
#     k = 0
#     for i in text:
#         if i.isnumeric():
#             k += 1
#     return k


# def left_join(phrases: tuple) -> str:
#     """
#     Join strings and replace "right" to "left"
#     """
#     stroke = ""
#     for i in phrases:
#         if phrases.index(i) + 1 != len(phrases):
#             stroke += i + ","
#         else:
#             stroke += i
#     if stroke.endswith(','):
#         stroke = stroke[::-1]
#         stroke = stroke.replace(',', '', 1)
#         stroke = stroke[::-1]
#     stroke = stroke.replace("right", "left")
#     return stroke
#
#
# print(left_join(("left", "right", "left", "stop")))


# def first_word(text: str) -> str:
#     """
#     returns the first word in a given text.
#     """
#     stroke = ''
#     for i in text:
#         if i.isalpha() or i == "'":
#             stroke += i
#         else:
#             if len(stroke) > 0:
#                 break
#     return stroke
#
#
# print(first_word("... and so on ..."))


# def romanToInt(s: str) -> int:
#     k = 0
#     roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     for indx, i in enumerate(s):
#         if indx < len(s) - 1:
#             if i == 'I' and (s[indx + 1] == 'V' or s[indx + 1] == 'X'):
#                 k -= roman[i]
#             elif i == 'X' and (s[indx + 1] == 'L' or s[indx + 1] == 'C'):
#                 k -= roman[i]
#             elif i == 'C' and (s[indx + 1] == 'D' or s[indx + 1] == 'M'):
#                 k -= roman[i]
#             else:
#                 k += roman[i]
#         else:
#             k += roman[i]
#     return k
#
# s ="MCMXCIV"
# print(romanToInt("MCMXCIV"))


# TODO НЕ ДОДЕЛАНО
# def isPalindrome(self, head: Optional[ListNode]) -> bool:
#     if len(list(head)) % 2 == 0:
#         lentgh = int(len(list(head)) / 2)
#         if head[lentgh:][::-1] == head[:lentgh]:
#             return True
#         else:
#             return False
#     else:
#         middle_index = int(len(list(head)) // 2 + 1)
#         if head[:middle_index] == head[middle_index - 1:][::-1]:
#             return True
#         else:
#             return False
#
#
# print(isPalindrome([1, 2, 3, 2, 1]))


# def days_diff(a, b):
#     from datetime import datetime
#     i = datetime(*a)
#     k = datetime(*b)
#     if i > k:
#         f = ''
#         z = i - k
#         for b in str(z):
#             if b.isnumeric():
#                 f += b
#             else:
#                 break
#         return f
#     else:
#         f = ''
#         z = k - i
#         for b in str(z):
#             if b.isnumeric():
#                 f += b
#             else:
#                 break
#         return f
#
# print(days_diff((2014, 8, 27), (2014, 1, 1)))


# def backward_string_by_word(text: str) -> str:
#     z = ''
#     my_list = []
#     for k, i in enumerate(text):
#         if i.isalpha() and k == len(text) - 1:
#             z += i
#             z = z[::-1]
#             my_list.append(z)
#             z = ''
#         elif i.isalpha():
#             z += i
#         elif i.isspace() and text[k-1].isalpha():
#             z = z[::-1]
#             z += i
#             my_list.append(z)
#             z = ''
#         elif i.isspace():
#             my_list.append(i)
#     stroke = ''.join(my_list)
#     return stroke
#
#
# print(backward_string_by_word('welcome to a game'))


# def maximumWealth(accounts) -> int:
#     my_list = []
#     for i in accounts:
#         z = 0
#         for k in i:
#             z += k
#         my_list.append(z)
#     return max(my_list)
#
#
# print(maximumWealth([[1,5],[7,3],[3,5]]))


# def between_markers(text: str, begin: str, end: str) -> str:
#     """
#           returns substring between two given markers
#       """
#     if begin not in text and end not in text:
#         return text
#     else:
#         if begin in text:
#             z = ''
#             b = 0
#             for i, k in enumerate(text):
#                 if k == begin[b]:
#                     z += k
#                     b += 1
#                 else:
#                     z = ''
#                     b = 0
#                 if z == begin:
#                     start = i + 1
#                     break
#         else:
#             start = 0
#         if end in text:
#             z = ''
#             b = 0
#             for i, k in enumerate(text):
#                 if k == end[b]:
#                     z += k
#                     b += 1
#                 else:
#                     z = ''
#                     b = 0
#                 if z == end:
#                     final = i - (len(end) - 1)
#                     break
#         else:
#             final = len(text) + 1
#             # text = text.replace(begin, '999')
#             # text = text.replace(end, '1000')
#         if all((begin in text, end in text)):
#             if text.index(begin) > text.index(end):
#                 return ''
#             else:
#                 return text[start:final]
#         else:
#             return text[start:final]
#
#
# print(between_markers('No <hi>', '>', '<'))


# def numberOfSteps(num: int) -> int:
#     k = 0
#     while num > 0:
#         if num % 2 == 0:
#             num /= 2
#             k += 1
#         else:
#             num -= 1
#             k += 1
#     return k
#
#
# print(numberOfSteps(14))


# def popular_words(text: str, words: list) -> dict:
#     text = text.lower()
#     my_words = []
#     word = ''
#     my_dict = {}
#     for k, i in enumerate(text):
#         if k == len(text) - 1:
#             word += i
#             my_words.append(word)
#             break
#         if i.isalpha() or i == "'":
#             word += i
#         if text[k+1].isspace():
#             my_words.append(word)
#             word = ''
#     for j in words:
#         my_dict[j] = my_words.count(j)
#     return my_dict


# def second_index(text: str, symbol: str) -> [int, None]:
#     """
#         returns the second index of a symbol in a given text
#     """
#     k = 0
#     for i in text:
#         if i == symbol:
#             if k == 1:
#                 return text.index(i) + 1
#             else:
#                 text = text.replace(i, '', 1)
#                 k += 1
#     if symbol not in text:
#         return None
#
#
# print(second_index("hi mr Mayor", " "))


# from typing import Union
#
#
# def sun_angle(time: str) -> Union[int, str]:
#     begin = int(time[0:2])
#     end = int(time[3:])
#     angle = ((begin - 6) * 15)
#     angle += round(float((end / 60) * 15), 2)
#     if end == 0:
#         angle = int(angle)
#     if angle > 180 or angle < 0:
#         return "I don't see the sun!"
#     return angle
#
#
# print(sun_angle("12:15"))


# def bigger_price(limit: int, data: list) -> list:
#     """
#         TOP most expensive goods
#     """
#     my_note = {}
#     for i in data:
#         my_note[i['name']] = i['price']
#     z = 0
#     f = ''
#     array = []
#     my_dict = {}
#     for _ in range(0, limit):
#         for k, b in my_note.items():
#             if b > z:
#                 z = b
#                 f = k
#         my_note[f] = 0
#         my_dict['name'] = f
#         my_dict['price'] = z
#         array.append(my_dict)
#         my_dict = {}
#         z = 0
#         f = ''
#     return array
#
#
# print(bigger_price(1, [{"name": "bread", "price": 100}, {"name": "wine", "price": 138},
#                        {"name": "meat", "price": 15}, {"name": "water", "price": 1}]))


# def split_list(items: list) -> list:
#     if len(items) == 0:
#         list_1 = []
#         list_2 = []
#         array = [list_1, list_2]
#         return array
#     elif len(items) % 2 == 0:
#         list_1 = items[:int(len(items) / 2)]
#         list_2 = items[int(len(items) / 2):]
#         array = [list_1, list_2]
#     elif len(items) % 2 != 0:
#         length = int(len(items) // 2 + 1)
#         list_1 = items[:length]
#         list_2 = items[length:]
#         array = [list_1, list_2]
#     return array
#
#
# print(split_list([]))


# from typing import List, Any
#
#
# def all_the_same(elements: List[Any]) -> bool:
#     if len(elements) == 0:
#         return True
#     z = elements[0]
#     for i in elements:
#         if i == z:
#             continue
#         else:
#             return False
#     return True


# def safe_pawns(pawns: set) -> int:
#     letters = 'abcdefgh'
#     safes = []
#     z = 0
#     for i in pawns:
#         letter = i[0]
#         number = int(i[1])
#         if letter != 'a' and letter != 'h':
#             safes.append(letters[letters.index(letter) + 1] + str(number + 1))
#             safes.append(letters[letters.index(letter) - 1] + str(number + 1))
#         elif letter == 'h':
#             safes.append(letters[letters.index(letter) - 1] + str(number + 1))
#         elif letter == 'a':
#             safes.append(letters[letters.index(letter) + 1] + str(number + 1))
#     for k in pawns:
#         if k in safes:
#             z += 1
#     return z
#
#
# print(safe_pawns({"a1","b2","c3","d4","e5","f6","g7","h8"}))


# def morse_decoder(code):
#     letter = ''
#     word = ''
#     phrases = ''
#     for k, i in enumerate(code):
#         if i == '.' or i == '-':
#             letter += i
#         if i == ' ' and letter != '':
#             word += MORSE[letter]
#             letter = ''
#         if i == ' ' and code[k + 1] == ' ' and code[k + 2] == ' ':
#             phrases += word + ' '
#             word = ''
#         if k == len(code) - 1:
#             word += MORSE[letter]
#             phrases += word
#     phrases = phrases.capitalize()
#     return phrases
#
#
# print(morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--"))


# def date_time(time: str) -> str:
#     months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
#               8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
#     cloak = ''
#     cloak += str(int(time[0:2]))
#     cloak += ' ' + months[int(time[3:5])]
#     cloak += ' ' + time[6:10] + ' year '
#     if time[11:13] == '01':
#         cloak += '1 hour '
#     else:
#         cloak += str(int(time[11:13])) + ' hours '
#     if time[14:] == '01':
#         cloak += '1 minute'
#     else:
#         cloak += str(int(time[14:])) + ' minutes'
#     return cloak
#
#
# print(date_time("21.10.1999 18:01"))


# def frequency_sort(items):
#     my_items = []
#     k = 0
#     for j in items:
#         if my_items:
#             if j in my_items:
#                 continue
#             else:
#                 if items.count(j) > items.count(my_items[k]):
#                     my_items.insert(k, j)
#                     k += 1
#                 else:
#                     my_items.append(j)
#                     k += 1
#         else:
#             my_items.append(j)
#     my_dict = {}
#     for i in items:
#         if i in my_dict:
#             continue
#         else:
#             my_dict[i] = items.count(i)
#     items.clear()
#     for j in my_items:
#         for _ in range(my_dict[j]):
#             items.append(j)
#
#     return items
#
#
# print(frequency_sort([4,6,2,2,2,6,4,4,4]))


# def replace_last(line: list) -> list:
#     if line:
#         last = line[-1]
#         line.remove(last)
#         line.insert(0, last)
#     return line
#
#
# print(replace_last([100]))


# def is_majority(items: list) -> bool:
#     k = 0
#     z = 0
#     if items:
#         for i in items:
#             if i:
#                 k += 1
#             else:
#                 z += 1
#         return True if k > z else False
#     else:
#         return False
#
#
# print(is_majority([]))


# def index_power(array: list, n: int) -> int:
#     if n >= len(array):
#         return -1
#     else:
#         return array[n] ** n
#
#
# print(index_power([1, 2], 3))


# def remove_all_after(items: list, border: int):
#     if border in items:
#         while len(items) - 1 > items.index(border):
#             if items:
#                 items.reverse()
#                 items.remove(items[0])
#                 items.reverse()
#         return items
#     else:
#         return items
#
#
# print(remove_all_after([10,1,5,6,7,10],5))


# from datetime import datetime
# from typing import List
#
#
# def sum_light(els: List[datetime]) -> int:
#     seconds = 0
#     for i in range(-len(els) + 1, 0, 2):
#         time = els[i] - els[i - 1]
#         seconds += time.total_seconds()
#     return seconds
#
#
# print(sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 0, 10),
#         datetime(2015, 1, 12, 11, 0, 0),
#         datetime(2015, 1, 13, 11, 0, 0),
#     ]))


# from typing import List
#
#
# def checkio(data: List[int]) -> [int, float]:
#     if len(data) % 2 == 0:
#         sorted_list = sorted(data)
#         length = int(len(sorted_list) / 2)
#         return (sorted_list[length] + sorted_list[length - 1]) / 2
#     else:
#         sorted_list = sorted(data)
#         return sorted_list[len(data)//2]
#
#
# print(checkio([3, 1, 2, 5, 3]))


# from typing import Iterable
#
#
# def except_zero(items: list) -> Iterable:
#     my_items = sorted(items)
#     while 0 in my_items:
#         my_items.remove(0)
#     while 0 in items:
#         my_items.insert(items.index(0), 0)
#         items.insert(items.index(0), '-')
#         items.remove(0)
#     return my_items
#
#
# print(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7]))


# from typing import List
#
#
# def frequency_sorting(numbers: List[int]) -> List[int]:
#     my_list = []
#     numbers = sorted(numbers)
#     dct_1 = {i: numbers.count(i) for i in numbers}
#     dct_2 = sorted(dct_1, key=dct_1.get, reverse=True)
#     for j in dct_2:
#         k = 0
#         while dct_1[j] > k:
#             my_list.append(j)
#             k += 1
#     return my_list
#
#
# print(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]))


# def reverse_ascending(items):
#     my_items = []
#     items_1 = []
#     z = 0
#     for i, k in enumerate(items):
#         if i == len(items) - 1:
#             my_items.append(k)
#             items_1.extend(sorted(my_items, reverse=True))
#             my_items = []
#         elif k > z:
#             my_items.append(k)
#             z = k
#         else:
#             items_1.extend(sorted(my_items, reverse=True))
#             my_items = []
#             my_items.append(k)
#             z = k
#     return items_1
#
#
# print(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3]))


# from typing import Iterable
#
#
# def compress(items: list) -> Iterable:
#     my_list = []
#     for i, k in enumerate(items):
#         if not my_list:
#             my_list.append(k)
#             continue
#         elif my_list[-1] == k:
#             continue
#         else:
#             my_list.append(k)
#     return my_list
#
#
# print(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0]))


# lst_1 = [2**x for x in range(1, 10)]
#
# dct_1 = {lst_1.index(a) + 1: a for a in lst_1}
#
# print(dct_1[5])


# class Backpack:
#     def __init__(self):
#         self.content = []
#
#     def add(self, item):
#         self.content.append(item)
#
#     def __len__(self):
#         return len(self.content) - 1
#
#     def __str__(self):
#         return 'Backpack: ' + ', '.join(self.content)
#
#     def __bool__(self):
#         return self.content != []
#
#
# my_backpack = Backpack()
# my_backpack.add('Кола')
# my_backpack.add('Пепси')
# my_backpack.add('Виски')
# print(len(my_backpack))
# print(bool(my_backpack))


# def flat_list(a):
#     q, o = [a], []
#     while q:
#         e = q.pop(-1)
#         q.extend(e) if type(e) == list else o.append(e)
#     return o[::-1]
#
#
# print(flat_list([1, 2, 3, [[5]],[6]]))

# from datetime import datetime
# from typing import List, Optional
#
#
# def sum_light(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
#     lst_1 = els[::]
#     if start_watching:
#         for k, i in enumerate(els):
#             if (start_watching - i).total_seconds() > 0:
#                 lst_1.remove(i)
#             else:
#                 lst_1.insert(0, start_watching)
#
#     return sum((d2 - d1).total_seconds() for d1, d2 in zip(*[iter(lst_1)]*2))
#
#
# print(sum_light([
# datetime(2015, 1, 12, 10, 0, 0),
# datetime(2015, 1, 12, 10, 10, 10),
# datetime(2015, 1, 12, 11, 0, 0),
# datetime(2015, 1, 12, 11, 10, 10)
# ]))


# lst_1 = []
# with open('F:\Downloads\9274620b-ec37-47b4-8856-22290819ea0d.txt', 'r') as F:
#     for _ in range(1, 5001):
#         s = F.readline()
#         lst_1.append(s[:-1])
# counter = 0
# my_max = -20000
# for i, k in enumerate(lst_1):
#     k = int(k)
#     if i == len(lst_1) - 1:
#         break
#     if k % 3 == 0 or int(lst_1[i+1]) % 3 == 0:
#         counter += 1
#         if my_max < k + int(lst_1[i + 1]):
#             my_max = k + int(lst_1[i + 1])
# print(counter, my_max)


# lst_1 = []
# with open('F:\Downloads\9fe53da1-84fc-4e97-aa87-f65fa6e5a7b8.txt', 'r') as F:
#     for _ in range(1, 10001):
#         if _ == 10000:
#             s = F.readline()
#             lst_1.append(s)
#         else:
#             s = F.readline()
#             lst_1.append(s[:-1])
#
# counter = 0
# my_max = -2000
# for i, k in enumerate(lst_1):
#     k = int(k)
#     if i == len(lst_1) - 1:
#         break
#     if (k * int(lst_1[i+1])) % 62 == 0:
#         counter += 1
#         if my_max < k + int(lst_1[i+1]):
#             my_max = k + int(lst_1[i+1])
# print(counter, my_max)


# lst_1 = []
# with open('F:\Downloads\9klok.txt', 'r') as F:
#     for i in range(1, 11001):
#         if i == 11000:
#             s = F.readline()
#             lst_1.append(s)
#         else:
#             s = F.readline()
#             lst_1.append(s[:-1])
# counter = 0
# my_max = - 20000
# print(lst_1)
# for i, k in enumerate(lst_1):
#     k = int(k)
#     if i == len(lst_1) - 1:
#         break
#     if (k + int(lst_1[i+1])) % 3 == 0:
#         if k % 17 == 0:
#             if int(lst_1[i+1]) % 17 == 0:
#                 counter += 1
#                 if k * int(lst_1[i+1]) > my_max:
#                     my_max = k * int(lst_1[i + 1])
# print(counter, my_max)


# class NewList(list):
#     def __getitem__(self, item):
#         if item > 0:
#             return super().__getitem__(item-1)
#         elif item < 0:
#             return super().__getitem__(item)
#
#
# b = NewList([2**a for a in range(1, 11)])
# print(b)
# print(b[0])


# сердечко из квадратиков
# import turtle
#
# pen = turtle.Turtle()
# pen.speed(0)
# pen.color("red")
# a = 20
#
#
# def sqard():
#     for i in range(4):
#         pen.forward(a)
#         pen.left(90)
#
#
# def love():
#     for i in range(75):
#         sqard()
#         pen.left(2)
#         global a
#         a = a + 2.5
#
#     for i in range(75):
#         sqard()
#         pen.left(2)
#         a = a - 2.5
#
#
# pen.penup()
# pen.left(75)
# pen.sety(150)
# pen.pendown()
# love()
#
# turtle.done()


# l1st = []
# with open('F:\Downloads\9999.txt', 'r') as F:
#     for _ in range(8000):
#         s = F.readline()
#         if s[:-1] not in l1st:
#             l1st.append(s[:-1])
# count = 0
# my_max = -99999
# for k, i in enumerate(l1st):
#     for j, z in enumerate(l1st[k+1:]):
#         i = int(i)
#         z = int(z)
#         if (i * z) % 2 == 1:
#             if (i % z == 0) or (z % i == 0):
#                 count += 1
#                 if z > i:
#                     if my_max < z:
#                         my_max = z
#                 else:
#                     if my_max < i:
#                         my_max = i
# print(count, my_max,)


# lst1 = []
# with open('F:\Downloads\978.txt') as F:
#     for _ in range(7000):
#         s = F.readline()
#         lst1.append(s[:-1])
#
# count = 0
# my_max = -9999
# for i, k in enumerate(lst1):
#     if i == len(lst1) - 1:
#         break
#     k = int(k)
#     z = int(lst1[i+1])
#     if (k % 123) != (z % 123):
#         if (k + z) % 123 == 0:
#             count += 1
#             if (k + z) > my_max:
#                 my_max = k + z
#
#
# print(count, my_max)


# for a in range(0, 1000):
#     b = 1
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             b *= (not(x <= 9) or (x * x <= a)) and (not(y * y <= a) or (y <= 9))
#             if not b:
#                 break
#     if b:
#         print(a)


# for a in range(1000):
#     b = 1
#     for x in range(1000):
#         for y in range(1000):
#             b *= (not(x < 6) or (x * x < a)) and (not(y * y <= a) or (y <= 6))
#             if not b:
#                 break
#     if b:
#         print(a)


# for a in range(1000):
#     b = 1
#     for x in range(1000):
#         for y in range(1000):
#             b *= (not(x < a) or (x * x < 81)) and (not(y * y <= 36) or (y <= a))
#             if not b:
#                 break
#     if b:
#         print(a)


# for a in range(1000):
#     b = 1
#     for x in range(1000):
#         b *= ((x & 29) == 0) or ((x & 12) != 0) or ((x & a) != 0)
#         if not b:
#             break
#     print(a) if b else None


# for a in range(1, 1000):
#     b = 1
#     for x in range(1, 1000):
#         b *= (x % a == 0) or (not(x % 10 == 0) or not(x % 18 == 0))
#         if not b:
#             break
#     if b and a < 50:
#         print(a)


# x = 9**8 + 3**5 - 9   #формула
# count2 = 0 #счетчик нужного нам числа
# while x: #пока x!=0
#     if x % 3 == 2: #делим x на основание в которой нужен ответ
#         count2 += 1 # прибавляем счётчик
#     x //= 3 # и делим нацело на основание
# print(count2)


# x = 4**2016 + 2**2018 - 8**600 + 6
# count1 = 0
# while x:
#     if x % 2 == 1:
#         count1 += 1
#     x //= 2
# print(count1)

# for a in range(1, 1000):
#     b = 1
#     for x in range(1, 1000):
#         b *= (x & 29 == 0) or ((x & 17 != 0) or (x & a != 0))
#         if not b:
#             break
#     if b:
#         print(a)


# lst = []
# with open('F:\Downloads\98876.txt', 'r') as F:
#     for _ in range(5000):
#         s = F.readline()
#         lst.append(s[:-1])
# counter = 0
# my_min = 9999
# for i, k in enumerate(lst):
#     for j, z in enumerate(lst[i+1:]):
#         k = int(k)
#         z = int(z)
#         if k % 5 == 0 or z % 5 == 0:
#             if (k * z) % (k + z) == 0:
#                 counter += 1
#                 if k + z < my_min:
#                     my_min = k + z
# print(counter, my_min)


# lst = []
# with open('F:\Downloads\9321.txt') as F:
#     for _ in range(6000):
#         s = F.readline()
#         lst.append(s[:-1])
#
# counter = 0
# my_min = 9999
# for i, k in enumerate(lst):
#     for z, j in enumerate(lst[i+1:]):
#         k = int(k)
#         j = int(j)
#         if (k+j) % 2 == 1:
#             if (k * j) % 125 == 0:
#                 counter += 1
#                 if my_min > k + j:
#                     my_min = k + j
# print(counter, my_min)


# lst = []
# with open('F:\Downloads\9666.txt', 'r') as F:
#     for _ in range(6000):
#         s = F.readline()
#         lst.append(s[:-1])
#
# counter = 0
# my_min = 9999
# for i, k in enumerate(lst):
#     k = int(k)
#     if i == len(lst) - 1:
#         break
#     if (k % 5 == 0) or (int(lst[i+1]) % 5 == 0):
#         counter += 1
#         if k + int(lst[i+1]) < my_min:
#             my_min = int(lst[i+1]) + k
# print(counter, my_min)


# with open("F:\Zona Dowlands\[HTML Academy] Профессиональный онлайн‑курс HTML и CSS,
# уровень 1 (2020)\Знакомство\Материалы.md", 'r', encoding='utf8') as F:
#     s = F.read()
#     print(s)


# print('xyzw')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (not(x == (not y)) or (y and not z)) or (z and not w)
#                 if not F:
#                     print(x, y, z, w)


# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (not x or (y == w)) or ((not z and x) == (z and w))
#                 if not F:
#                     print(x, y, z, w)


# s = 127 * '9'
# while '333' in s or '999' in s:
#     if '333' in s:
#         s = s.replace('333', '9', 1)
#     else:
#         s = s.replace('999', '3', 1)
# print(s)


# s = 54 * '5' + '7'
# while '722' in s or '557' in s:
#     if '722' in s:
#         s = s.replace('722', '57', 1)
#     else:
#         s = s.replace('557', '72', 1)
# print(s)


# s = '1' + 100 * '9'
# while '19' in s or '299' in s or '3999' in s:
#     s = s.replace('19', '2', 1)
#     s = s.replace('299', '3', 1)
#     s = s.replace('3999', '1', 1)
# print(s)


# s = 7 * '1' + 7 * '2'
# while '111' in s or '222' in s:
#     if '111' in s:
#         s = s.replace('111', '2', 1)
#     if '222' in s:
#         s = s.replace('222', '1', 1)
# print(s)


# s = 80 * '1'
# while '11111' in s:
#     s = s.replace('111', '2', 1)
#     s = s.replace('222', '1', 1)
# print(s)


# print('w x y z')
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 F = (x and not y) or (y == z) or not w
#                 if not F:
#                     print(w, x, y, z)


# s = 100
# n = 300
# while s + n <= 500:
#     s = s + 30
#     n = n - 20
# print(s)


# x = 25**5 + 5**14 - 5
# counter = 0
# while x:
#     if x % 5 == 4:
#         counter += 1
#     x //= 5
# print(counter)


# for a in range(1, 64):
#     b = 1
#     for x in range(1, 100):
#         b *= (x & 51 == 0) or ((x & 41 != 0) or (x & a == 0))
#         if not b:
#             break
#     if b:
#         print(a)


# def F(n):
#     if n >0:
#         print(n, end='')
#         F(n // 2)
#         F(n - 4)
#
# F(9)


# lst = []
# with open('F:\Downloads\998.txt', 'r') as F:
#     for _ in range(6000):
#         s = F.readline()
#         lst.append(s[:-1])
#
# counter = 0
# my_max = -9999
# for i, k in enumerate(lst):
#     for z, j in enumerate(lst[i+1:]):
#         k = int(k)
#         j = int(j)
#         if (k * j) % (k + j) == 0:
#             if (k % 2 == 0) and (j % 2 == 0):
#                 counter += 1
#                 if (k * j) > my_max:
#                     my_max = k * j
# print(counter, my_max)


# for k, x in enumerate(range(1000)):
#     a = 0
#     b = 10
#     while x > 0:
#         c = x % 10
#         a += c
#         if c < b:
#             b = c
#         x //= 10
#     if a == 11 and b == 5:
#         print(k)


# import json
#
#
# def greetings():
#     try:
#         with open('username.json') as f_obj:
#             username = json.load(f_obj)
#             print(f'Здравствуйте, {username}!')
#     except FileNotFoundError:
#         with open('username.json', 'w') as f_obj:
#             username = input('Мы вас не знаем введите своё имя ')
#             json.dump(username, f_obj)
#             print(f'Вы вас запомнили, {username}')
#
#
# greetings()


# print('x y z')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             F = (x and y and not z) or (x and y and z) or (x and not y and not z)
#             if F:
#                 print(x, y, z)


# n = 1
# s = 0
# while n <= 300:
#     s = s + 30
#     n = n * 3
# print(s)


# counter = 0
# letters = 'ЗИМА'
# for a in letters:
#     for b in letters:
#         for c in letters:
#             for d in letters:
#                 for f in letters:
#                     word = a + b + c + d + f
#                     if (word[0] == 'З' or word[0] == 'М') and (word[4] == 'А' or word[4] == 'И'):
#                         counter += 1
# print(counter)


# a = '1' + 98 * '9'
# while '19' in a or '299' in a or '3999' in a:
#     a = a.replace('19', '2', 1)
#     a = a.replace('299', '3', 1)
#     a = a.replace('3999', '1', 1)
# print(a)


# def F(n):
#     if n > 0:
#         print(n, end='')
#         F(n - 4)
#         F(n // 2)
#
# F(9)


lst_1 = []
with open('F:\\Downloads\\962.txt', 'r') as file:
    for line in file:
        lst_1.append(line[:-1])


# counter = 0
# my_max = -999999
# for i, k in enumerate(lst_1):
#     for z, j in enumerate(lst_1[i+1:]):
#         k = int(k)
#         j = int(j)
#         if (k + j) % 10 == 0:
#             counter += 1
#             if (k + j) > my_max:
#                 my_max = (k + j)
# print(counter, my_max)


# for x in range(1, 10000):
#     L = 0
#     M = 0
#     y = str(x)
#     while x > 0:
#         L += 1
#         if x % 2 == 0:
#             M = M + (x % 10) // 2
#         x = x // 10
#     if L == 3 and M == 7:
#         print(y)


# def reverse_string(s) -> None:
#     """
#     Do not return anything, modify s in-place instead.
#     """
#     for i in range(len(s)):
#         s.insert(i, s.pop(-1))
#
#
# s = ['y', 'i', 'e', 'l', 'd']
# reverse_string(s)
# print(s)


# print('w x y z')
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 F = (x and not y) or (x == z) or not w
#                 if not F:
#                     print(w, x, y, z)


# s = 85 * '7'
# while '333' in s or '777' in s:
#     if '333' in s:
#         s = s.replace('333', '7', 1)
#     else:
#         s = s.replace('777', '3', 1)
# print(s)


# print('x y z')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             F = (not z) and x
#             if F:
#                 print(x, y, z)


# for x in range(10000):
#     f = str(x)
#     L = 0
#     M = 0
#     while x > 0:
#         L = L + 1
#         if x % 2 == 0:
#             M = M + x % 10
#         x = x // 10
#     if L == 3 and M == 8:
#         print(f)
#         break


# for x in range(10000, 1, -1):
#     f = str(x)
#     l = 0
#     m = 1
#     while x > 0:
#         l += 1
#         if x % 2 > 0:
#             m *= x % 8
#         x = x // 8
#     if m == 25 and l == 3:
#         print(f)
#         break


# for x in range(10000):
#     f = str(x)
#     a = 0
#     b = 0
#     while x > 0:
#         if x % 2 == 0:
#             a += 1
#         else:
#             b += x % 6
#         x = x // 6
#     if a == 2 and b == 4:
#         print(f)
#         break


# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = ((not w or not x) == (not z or y)) and (y or w)
#                 if F:
#                     print(x, y, z, w, bool(F))
#                 else:
#                     print(x, y, z, w, bool(F))


# print('x y z')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             F = (not z) and x or x and y
#             print(z, y, x, bool(F))


# print('w x y z')
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 F = (x and not y) or (x == z) or not w
#                 if not F:
#                     print(w, z, y, x)


# s = 70 * '8'
# while '2222' in s or '8888' in s:
#     if '2222' in s:
#         s = s.replace('2222', '88', 1)
#     else:
#         s = s.replace('8888', '22', 1)
# print(s)


# for x in range(101, 10000):
#     f = str(x)
#     L = x - 30
#     M = x + 30
#     while L != M:
#         if L > M:
#             L = L - M
#         else:
#             M = M - L
#     if M == 30:
#         print(f)
#         break


# for x in range(1, 10000):
#     f = str(x)
#     a = 0
#     b = 0
#     while x > 0:
#         c = x % 10
#         a += c
#         if c > b:
#             b = c
#         x //= 10
#     if a == 9 and b == 5:
#         print(f)
#         break
