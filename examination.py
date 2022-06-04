#2_1
# nums = input("Введите числа: ").split()
# for i in nums:
#     if nums.count(i) == 1:
#         print(i)

#2_2
# nums = input("Введите элементы: ").split()
# s = set(nums)
# print(f"Всего пар элементов в списке: {len(nums) - len(s)}")

#2_3
# c_1 = tuple(int(i) for i in [35, 78, 21, 37, 2, 98, 6, 100, 231])
# c_2 = tuple(int(i) for i in [45, 21, 124, 76, 5, 23, 91, 234])
# с_1_max = max(c_1)
# с_2_max = max(c_2)
# с_1_min = min(c_1)
# с_2_min = min(c_2)
# if sum(c_1) > sum(c_2):
#     print(f"Сумма больше в кортеже {c_1}")
# else:
#     print(f"Сумма больше в кортеже {c_2}")
# print(f"В кортеже c_1 минимальный элемент {c_1.index(с_1_min)}, максимальный элемент {c_1.index(с_1_max)}")
# print(f"В кортеже c_2 минимальный элемент {c_2.index(с_2_min)}, максимальный элемент {c_2.index(с_2_max)}")

#2_4
# str = 'An apple a day keeps the doctor away'
# new = {i : str.count(i) for i in str}
# print(new)

#2_5
menu = {"Наполеон" : ["Масло, мука, сахар", 3, 1500], "Киевский" : ["Масло, мука, шоколад", 4, 2800], "Медовик" : ["Сметана, мука, мёд", 5, 3100]}
cake = input("Какой торт Вы хотели бы приобрести: ").capitalize()
action = input("Что Вы хотели бы уточнить: ").capitalize()
for k, v in menu.items():
    if k == cake:
        if action == "Описание":
            print(f"Торт {k} состоит из: {v[0]}")
            quant = int(input("Сколько граммов торта вам положить: "))
            price = quant * int(v[1]) / 100
            print(f"К оплате {price} рублей")
            print(f"Торта {k} осталось {int(v[-1] - quant)} грамм")
        elif action == "Цена":
            print(f"Торт {k} стоит {v[1]} рублей за 100 грамм")
        elif action == "Количество":
            print(f"Торт {k} осталось {v[-1]} грамм")
        else:
            print("Ошибка. Проверьте введённые данные")

#2_6
# ln_1 = set(int(i) for i in input("Введите числа: ").split())
# ln_2 = set(int(i) for i in input("Введите числа: ").split())
# print(f"Количество одинаковых чисел в списке: {len(ln_1.intersection(ln_2))}")

#2_7
#Программа расчитывает сумму, которую нужно заплатить за определённый вес продукта
# try:
#     num_1 = int(input("Введите количество грамм продукта: "))
#     num_2 = int(input("Введите сумму за 100 грамм продукта: "))
#     print(f"Итого к оплате: {num_1 * num_2 / 100} рублей")
# except ValueError:
#     print("Вы ввели букву либо знак. Пожалуйста, введите число")
# finally:
#     print("Спасибо за то, что воспользовались нашей услугой")
#
#2_8
# grades = 0
# quant = 0
# with open ("grades.txt", "r") as file:
#     for line in file:
#         line = line.rstrip()
#         grades += int(line[-1])
#         quant += 1
#         if int(line[-1]) < 3:
#             print(line)
# print(f"Средняя оценка за тест = {grades / quant}")


