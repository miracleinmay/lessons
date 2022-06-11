#13_1
# Напишите функцию Python, чтобы найти максимум трех чисел.

# def sum_three(n1,n2,n3):
#     return max(n1,n2,n3)
#

# n1 = int(input("Enter the number: "))
# n2 = int(input("Enter the number: "))
# n3 = int(input("Enter the number: "))
# print(f"Max number: {sum_three(n1,n2,n3)}")

#13_2
# Напишите функцию Python для суммирования всех чисел в списке

# def sum_nums(numbers):
#     summ = 0
#     for i in numbers:
#         summ += i
#     return summ
#
#
# print(sum_nums([int(i) for i in input("Enter the numbers: ").split()]))

#13_3
# Напишите функцию Python для умножения всех чисел в списке

# def mult_nums(numbers):
#     mult = 1
#     for i in numbers:
#         mult *= i
#     return mult
#
#
# print(mult_nums([int(i) for i in input("Enter the numbers: ").split()]))

#explanation
# def mult_nums(*args): #args - все значения будут в этом параметре, выдаётся кортеж
#     mult = 1
#     for i in args:
#         mult *= i
#     return mult
#
# print(mult_nums(2, 2, 1, 3, 4))

#13_5
# Напишите функцию count_args,которая принимает произвольное количество аргументов.
# Данная функция должна возвращать количество переданных ей на вход аргументов

# def len_str(*nums):
#     return len(nums)
#
#
# print(f"The length of the string = {len_str(2,3,4,5)}")

#Explanation
# def mult_nums(**kwargs): #kwargs -  собирает именованные аргументы в словарь
#     for k, v in kwargs.items():
#         print(k, v, sep="-->")
#
#
# print(mult_nums(number =1, letter = "a"))

#13_4
# Создайте функцию count_letters, которая принимает на вход фразу и подсчитывает,
# какое количество в ней строчных(down) и заглавных (up) букв.
# Функция должна вывести на экран информацию о найденных буквах в определенном формате.
# Количество заглавных символов: up
# Количество строчных символов: down

# def letter(string):
#     up = 0
#     down = 0
#     for i in string:
#         if i.isupper():
#             up += 1
#         elif i.islower():
#             down += 1
#         else:
#             pass
#     print(f"Количество заглавных символов: {up}")
#     print(f"Количество строчных символов: {down}")
#
#
# letter(input("Enter something: "))


#13_6
# Напишите функцию info_kwargs, которая принимает произвольное количество именованных аргументов.
# Функция info_kwargs должна распечатать именованные аргументы в каждой новой
# строке в виде пары <Ключ> = <Значения>, причем ключи должны следовать в
# алфавитном порядке.

# def info_kwargs(**kwargs):
#     for k, v in sorted(kwargs.items()):
#         print(k, v, sep=" = ")
#
#
# print(info_kwargs(num_1 = 3, letter = "2", w = 4, a = 9))

#Документация функции (для того, чтобы посмотреть, что делает функция)
# def funt():
#     """
#     считает сумму двух чисел
#     а = первое слагаемое
#     б = второе слагаемое
#     return = сумма двух чисел
#     """
#
#Замыкания - функции в функциях


