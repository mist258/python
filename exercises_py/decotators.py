# ##Створіть простий контекстний менеджер file_opener за допомогою декоратора з contextlib, який буде відкривати файл, повертати його та закривати при виході з контексту
# Приклад використання:
# with file_opener("file.txt", "r") as f:
# f.read()
# from contextlib import contextmanager
#
#
# @contextmanager
# def file_opener(filename, mode):
#     file = None
#     try:
#         file = open(filename, mode)
#         yield file
#     except FileNotFoundError as err:
#         print(err)
#         yield None
#     finally:
#
#         file.close()
#
#
# with file_opener('file1.txt', 'r') as file:
#     print(file.read())



# # Напишіть простий декоратор, який буде прінтити повідомлення “Function is been called” до та після виклику функції.
# # Будьте уважні, деворатор повинен працювати з усіма функціями, які приймають різні параметри, та не забувайте повертати результат роботи функції.
# # Приклад використання:
# # @called_decorator
# # def some_func(1, b, c):
# #     ...
# #     some code
# # #     ...
#
# def called_decorator(func):
#     def inner(*args, **kwargs):
#         print('Function is been called')
#         res = func(*args, **kwargs)
#         print(res)
#         print('Function is been called')
#         return res
#     return inner
#
#
# @called_decorator
# def triangle_area(a, b, c):
#     return a*b*c
#
#
# triangle_area(2, 3, 4)
#
#
# # Напишіть декоратор, який буде прінтити “{імʼя функції яку викликали} is been called with parameters: {список параметрів з якими функцію викликали}”,
# # а після виклику функції “Function {function_name} return this value: {значення яке функція повернула}”
# # Приклад використання:
# # @function_info
# # def some_func(a, b, c):
# #     ...
# #     code
# #     return ...
# import math
#
#
# def function_info(func):
#     def inner(*args, **kwargs):
#         print(f'{func.__name__} is being called with parameters: {args}')
#         res = func(*args, **kwargs)
#         print(res)
#         print(f'Function{func.__name__} return this value {res}')
#         return res
#     return inner
#
#
# @function_info
# def pythagoras_theorem(a, b):
#     return math.sqrt(a**2 + b**2)
#
#
# pythagoras_theorem(3, 4)



# # Напишіть декоратор, який приймає як параметр число, та робить time.sleep перед викликом декорованої функції на це число.
# # Приклад використання:
# # @sleeper(5)
# # def some_func(a, b, ...):
# #     ...
#
# import time
#
#
# def sleeper(n):
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             time.sleep(n)
#             return func(*args, **kwargs)
#         return inner
#     return wrapper
#
#
# @sleeper(2)
# def print_word():
#     print(input('Enter any word:'))
#
#
# print_word()


# # Напишіть декоратор, який буде приймати необмежену кількість типів даних (str, int і так далі) та перевіряти аргументи які передали в декоровану функцію на те чи вони є типами,
# # які передали в декоратор, та повертати помилку якщо ні. Наприклад ми передали @my_decorator(int, str) а декоровану функцію викликали з аргументами func(2, “hello”, True)
# # повинна повернутись помилка бо ми не очікуємо bool тип.
# # Приклад використання:
# # @type_checker(int, str)
# # def some_func(a, b, c):
# #     ...
#
#
# def my_decorator(*args1):
#     def wrapper(func_types):
#         def inner(*args):
#             types_list = [*args1]
#             func_types(*args)
#             res = [*args]
#             for el in res:
#                 if type(el) in types_list:
#                     print(f'type {type(el)} in list')
#                 else:
#                     print(f'type {type(el)} not in list')
#
#         return inner
#     return wrapper
#
#
# @my_decorator(int, str, bool)
# def data_types(*args):
#     return args
#
#
# data_types(2, 'hello', True, 2.0)
