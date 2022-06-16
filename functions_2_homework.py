# Hometask_13_4
# Напишите функцию, которая  создает список случайных
# элементов. На фход функция принимает кол-во элементов, минимальное и максимальное значение
# In: rand_nums(7, 2, 12)
# Out: [12, 6, 9, 2, 11, 5, 8]
import random
#
#
# def rand_nums(quant, min, max):
#     return list(map(lambda i: random.randint(min,max), range(1, quant + 1)))
#

# print(rand_nums(7,2,12))

# Hometask_13_5
# Преобразуйте задачу с покупкой торта из экзамена 2 в функцию.

# menu = {"Наполеон" : ["Масло, мука, сахар", 3, 1500], "Киевский" : ["Масло, мука, шоколад", 4, 2800], "Медовик" : ["Сметана, мука, мёд", 5, 3100]}
#
# def cakes(what_cake, what_to_do):
#     for k, v in menu.items():
#         if k == what_cake:
#             if what_to_do == "Описание":
#                 print(f"Торт {k} состоит из: {v[0]}")
#                 quant = int(input("Сколько граммов торта вам положить: "))
#                 price = quant * int(v[1]) / 100
#                 print(f"К оплате {price} рублей")
#                 print(f"Торта {k} осталось {int(v[-1] - quant)} грамм")
#             elif action == "Цена":
#                 print(f"Торт {k} стоит {v[1]} рублей за 100 грамм")
#             elif action == "Количество":
#                 print(f"Торт {k} осталось {v[-1]} грамм")
#             else:
#                 print("Ошибка. Проверьте введённые данные")
#
#
# cake = input("Какой торт Вы хотели бы приобрести: ").capitalize()
# action = input("Что Вы хотели бы уточнить: ").capitalize()
# print(cakes(cake,action))

# Hometask_13_6
# Напишите функцию, вычисляющую значение факториала числа N. Используйте рекурсию.
# In: 5
# Out: 120

# def factorial(num):
#     if num == 1:
#         return 1
#     return factorial(num-1)*num
#
#
# print(factorial(5))