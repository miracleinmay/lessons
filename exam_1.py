#exam_1_1
# num = input("Enter the number: ")
# even = 0
# odd = 0
# sum = 0
# first = num[0]
# third = num[2]
# sixth = num[5]
# while int(num) != 0:
#     last = int(num) % 10
#     if last % 2 == 0:
#         even += 1
#         sum += last
#     elif last % 2 != 0:
#         odd += 1
#     num = int(num) // 10
# if even > odd:
#     print(f"Четных цифр больше, сумма цифр числа = {sum}")
# else:
#     mult = int(first) * int(third) * int(sixth)
#     print(f"Нечетных цифр больше, произведение {first}, {third}, {sixth} = {mult}")
# # #
#exam_1_2
# str = input("Enter the words: ").lower()
# vowels = "euioa"
# vows = 0
# cons = 0
# string = []
# for i in str:
#     if i.isalpha() and i in vowels:
#         vows += 1
#         string.append(i)
#     elif i.isalpha() and i not in vowels:
#         cons += 1
# print(f"Гласных букв: {vows}\nСогласных букв: {cons}")
# if vows == cons:
#     print(string)

#exam_1_3
import random

# iter = 1
# a_more_r1 = 0
# b_more_r2 = 0
# while iter <= 6:
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
#     r1 = random.randint(1,20)
#     r2 = random.randint(1,20)
#     if a > r1:
#         a_more_r1 += 1
#     if b > r2:
#         b_more_r2 += 1
#     iter += 1
#     if iter == 4:
#         chis1 = r1
#         chis2 = r2
# if a_more_r1 == b_more_r2:
#     print(f"Рандомные числа, полученные в 4-ой итерации {chis1}, {chis2}"
# else:
#     print(f"A > r1 {a_more_r1} раз\nB > r2 {b_more_r2} раз")


#exam_1_4
# import random
#
#
# num = int(input("Какую цифру будем искать: "))
# quant = int(input("Сколько раз будем искать эту цифру: "))
# iter = 1
# all = 0
# while iter <= quant:
#     anothernum = random.randint(1,20)
#     while anothernum:
#         last = anothernum % 10
#         if last == num:
#             all += 1
#         anothernum = anothernum // 10
#     iter += 1
# print(f"Цифра {num} встретилась {all} раз(a)")

#exam_1_5
# str = input("Enter something: ")
# num = [print(i) for i in str if i.isdigit() and int(i) > 0]

#exam_1_6
# str = input("Enter something: ")
# coupleup = 0
# coupledown = 0
# cons = 0
# vows = 0
# alph = 0
# vowels = "euioaEUIOA"
# for i in str:
#     if i.isalpha():
#         if i in vowels:
#             vows += 1
#         elif i not in vowels:
#             cons += 1
# if i.isalpha():
#     for i in range(1, len(str)):
#         if  str[i-1].islower() and str[i].islower():
#             coupledown += 1
#         elif str[i-1].isupper() and str[i].isupper():
#             coupleup += 1
# all = vows + cons
# print(f"Пар верхнего регистра: {coupleup}\nПар нижнего регистра: {coupledown}\nГласных букв {vows}\nCогласных букв {cons}\nBсего букв {all}")