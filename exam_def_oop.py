# exam_3_1
# Напишите функцию, которая будет принимать номер кредитной карты и показывать
# только последние 4 цифры.Остальные цифры должны заменяться звездочками.

# def credit_card(number):
#     card_number = '*' * (len(number)-4) + number[-5:-1]
#     print(card_number)
# 
# credit_card(input("Введите номер кредитной карты: "))

# exam_3_2
# Напишите функцию, которая
# проверяет: является ли слово
# палиндромом

# def palindrom(word):
#     if word == word[::-1]:
#         return True
#     return False
#
# print(palindrom(input("Введите слово: ")))

# exam_3_
# Напишите классы Круг, Прямоугольник, Квадрат.
# Каждый класс должен содержать метод нахождения площади фигуры.
# Используйте:
# - Наследование
# - Абстрактный классvи методы
# - Округлите площадь круга до 2х чисел после запятой
# - Число π возьмите из модуля

# from abc import ABC, abstractmethod
# from math import pi
# 
#
# class Figures(ABC):
#
#     @abstractmethod
#     def area(self):
#         pass
#
#
# class Circle(Figures):
#
#     def __init__(self, rad):
#         self.rad = rad
#
#     def area(self):
#         result = self.rad ** 2 * pi
#         return f"Площадь круга равна {round(result, 2)}"
#
# class Square(Figures):
#
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return f"Площадь квадрата равна {self.side ** 2}"
#
#
# class Rectangle(Figures):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         ar = self.length * self.width
#         return f"Площадь прямоугольника равна {ar}"
#
#
# square = Square(4)
# rectangle = Rectangle(2, 6)
# circle = Circle(3)
#
#
# figures = [square, rectangle, circle]
#
# for i in figures:
#     print(i.area())


