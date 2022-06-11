#Hometask_13_1
# Из полученного списка чисел создайте список с суммами этих чисел, отсортированными по возрастанию
# In: 965 582 023 8 695210
# Out: [5, 8, 15, 20, 23]

# def sum_digits(nums):
#     new_sum = []
#     for number in nums:
#         sum = 0
#         while number != 0:
#             left = number % 10
#             sum += left
#             number = number // 10
#         new_sum.append(sum)
#     return sorted(new_sum)
#
#
# try:
#     print(sum_digits([int(i) for i in input("Enter numbers: ").split()]))
# except ValueError:
#     print("Ошибка. Проверьте правильность написания (вам нужно ввести число)")

# Hometask_13_2
# Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей
# числовой прямой.

# def func_x(x):
#     if x <= -2:
#         result = 1 - (x+2)**2
#     elif -2 < x <= 2:
#         result = -(x / 2)
#     elif 2 < x:
#         result = (x-2)**2 + 1
#     return result
#

# try:
#     print(func_x(float(input("Введите число: "))))
# except ValueError:
#     print("Ошибка. Проверьте правильность написания (вам нужно ввести число)")

# Hometask_13_3
# Напишите функцию которая принимает на вход список целых чисел, удаляет из него
# все нечётные значения, а чётные нацело делит на два.
# In: 852 85 784 58
# Out: [426, 392, 29]

# def even_nums(list_nums):
#     new_list = []
#     for i in list_nums:
#         if i % 2 == 0:
#             i = i // 2
#             new_list.append(i)
#     return new_list
#
# try:
#   print(even_nums([int(i) for i in input("Enter numbers: ").split()]))
# except ValueError:
# #     print("Ошибка. Проверьте правильность написания (вам нужно ввести число)")

# ИЛИ МЕТОД БЕЗ СОЗДАНИЯ НОВОГО СПИСКА

# def even_nums(list_nums):
#     for i in list_nums:
#         if i % 2 != 0:
#             list_nums.remove(i)
#         else:
#             i = i // 2
#     return list_nums
#
# try:
#     print(even_nums([int(i) for i in input("Enter numbers: ").split()]))
# except ValueError:
#     print("Ошибка. Проверьте правильность написания (вам нужно ввести число)")