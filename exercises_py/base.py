# function
# Напишіть функцію, яка возводить перше число у ступінь другого числа і повертає результат.
# def func_exponentiation(num):
#     exp = num ** (num+1)
#     return exp
#
#
# num = int(input("Enter a number: "))
# print(func_exponentiation(num))

# Напишіть функцію, яка приймає список чисел і повертає новий список, в якому всі числа помножені на 2.


# def func_multiple_list(list_num):
#     for i in range(len(list_num)):
#         list_num[i] = list_num[i] * 2
#     print(list_num)
#
#
# list_num = []
# numbers = int(input("Enter a number: "))
# for i in range(numbers):
#     list_num.append(int(input("Enter a number: ")))
#
# func_multiple_list(list_num)

# Напишіть функцію, яка приймає рядок і повертає кількість голосних літер у цьому рядку.


# def func_wolves(line):
#     wolves = ['a','o','y','u','i','e']
#     count = 0
#     for ch in line:
#         if ch in wolves:
#             count += 1
#     print(count)
#
#
# line = 'hello world'
# func_wolves(line)

#Напишіть функцію, яка приймає список чисел і повертає список, що містить лише парні числа.

# def funct_list_numbers(list_numbers):
#     even_numbers = []
#     for number in list_numbers:
#         if number % 2 == 0:
#             even_numbers.append(number)
#     print(even_numbers)
#     return even_numbers
#
# list_numbers = [1, 2, 56,55, 34, 25,89, 45, 7, 8]
# funct_list_numbers(list_numbers)

#Напишіть функцію, яка приймає рядок і повертає його у зворотньому порядку (саме слова, як показано в прикладі).

# def funct_reverse(str_line):
#     new_line = str_line.split()
#     new_line.reverse()
#     print(' '.join(new_line))
#
#
# str_line = 'Hello world!'
# funct_reverse(str_line)

#Напишіть функцію, яка отримує кілька слів як аргументи і повертає словник, що містить кількість кожної голосної літери у ВСІХ словах.
# Використовуйте метод count для підрахунку входжень кожної голосної. Наприклад результат роботи функциії {”a”: 13, “e”: 4, “o”: 23, “i”: 2}

# def funct_words(*args):
#     wolves = ['a','e', 'i', 'o', 'u', 'y']
#     count_a = 0
#     count_e = 0
#     count_i = 0
#     count_o = 0
#     count_u = 0
#     count_y = 0
#     for v in (args):
#         for ch in v:
#             if ch == 'a':
#                 count_a += 1
#             elif ch == 'e':
#                 count_e += 1
#             elif ch == 'i':
#                 count_i += 1
#             elif ch == 'o':
#                 count_o += 1
#             elif ch == 'u':
#                 count_u += 1
#             elif ch == 'y':
#                 count_y += 1
#     general_count = count_a, count_e,  count_i,  count_o,  count_u, count_y
#     dict_letters = {k:v for k,v in zip(general_count, wolves)}
#     print(dict_letters)
#
#
# str1 = 'Hello'
# str2 = 'World'
# str3 = 'Python'
# str4 = 'Continue'
# funct_words(str1, str2, str3, str4)

#Напишіть функцію, яка отримує речення у вигляді рядка і повертає нове речення,
# в якому перша буква кожного слова пишеться з великої літери. Використовуйте метод split, щоб розбити речення на слова, і метод capitalize, щоб зробити першу літеру великою.

#Напишіть функцію, яка отримує необмежену кількість рядків як аргументи і повертає один об'єднаний рядок.

#Створіть функцію, яка приймає список слів і повертає список слів, які містять п'ять або більше літер та починаються з голосної (a, e, i, o, u).

#Напишіть функцію, яка отримує речення як рядок і повертає кількість слів у цьому реченні.

#Напишіть функцію, яка приймає на вхід два словника. Значення у словника обовʼязково число. Задача повернути новий словник, де будуть всі ключі з першого та другого словника,
#а у випадку якщо ключ є і там і там потрібно додати значення за цим ключем в першого та другого словника до результату.

#Напишіть функцію, яка приймає два рядки і повертає True, якщо вони є анаграмами (тобто містять однакові букви в різному порядку), і False - в іншому випадку.

#Напишіть функцію, яка обчислює факторіал заданого числа і повертає результат.

#Напишіть функцію, яка перевіряє, чи є задане число простим, і повертає True або False.

#Напишіть функцію, яка приймає список чисел і повертає найбільше число зі списку. Функцію max використовувати не можна.

#Напишіть функцію, яка приймає список рядків і повертає новий список, в якому всі рядки переведені у верхній регістр.

