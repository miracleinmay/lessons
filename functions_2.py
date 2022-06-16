from functools import reduce



#13_7
# Напишите программу, которая возводит в куб каждое число из полученного списка чисел
# пользуясь при этом функциями map и lambda.
# In: 2 4 7 1
# Out: [8, 64, 343, 1]

# ls = list(map(int, input().split()))
# mult = list(map(lambda i: i**3, ls))
# print(mult)

#13_8
# На вход программа получает список, состоящий из отрицательных, положительных
# чисел и нулей. При помощи функций filter, len, lambda определить сколько в
# списке чисел отрицательных значений, сколько нулей и сколько положительных.
# In: 2 45 -45 0 0 -3 -36 34 34 46
# Out: 3
# 2
# 5

# ls = list(map(int, input().split()))
# pos_nums_1 = len(list(filter(lambda i: i>0, ls)))
# nums_1 = len(list(filter(lambda i: i<0,ls)))
# zero = len(list(filter(lambda i: i==0, ls)))

#13_9
# На вход программа получает 2  числа через пробел, не иначе! Выведите сумму этих двух чисел.
# Воспользуйтесь функцией map
# In: 2 4
# Out: 6
#
# a,b = map(int, input().split())
# print(a+b)

# n = int(input())
# ls = [int(input()) for i in range(n)]
# def last(count,lst):
#     if count != 0:
#         print(lst[count-1])
#         last(count-1, lst)
#
# print(last(n,ls))




# def dec_div(div_funct):
#     def wrapper(n1, n2):
#         return n2/n1
#         div_funct(n1,n2)
#     return wrapper
#
#
# @dec_div
# def div(x,y):
#     return x/y
#
# print(div(2,4))

#
# def bank(money,year):
#     while year:
#         money += money * 0.1
#         year -=1
#     return money
#
# print(bank(200, 4))