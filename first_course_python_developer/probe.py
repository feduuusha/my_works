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


from datetime import datetime
from typing import List, Optional


def sum_light(els: List[datetime], start_watching: Optional[datetime] = None,
              end_watching: Optional[datetime] = None) -> int:
    lst_1 = els[::]
    if start_watching:
        for i in els:
            if (start_watching - i).total_seconds() >= 0:
                lst_1.remove(i)
            else:
                lst_1.insert(0, start_watching)
    if end_watching:
        for i in els[::-1]:
            if (i - end_watching).total_seconds() > 0:
                lst_1.remove(i)
            else:
                lst_1.insert(len(lst_1), end_watching)
                break
    if len(lst_1) >= 1 and len(els) % 2 == 0:
        return sum((d2 - d1).total_seconds() for d1, d2 in zip(*[iter(lst_1)]*2))
    else:
        lst_1.clear()
        lst_1.append(start_watching)
        lst_1.append(end_watching)
        return sum((d2 - d1).total_seconds() for d1, d2 in zip(*[iter(lst_1)] * 2))


print(sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
    datetime(2015, 1, 12, 10, 0, 10),
    datetime(2015, 1, 12, 10, 0, 20)))

