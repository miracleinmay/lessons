# Hometask_14_1
# Создать класс Dog.
# Класс имеет четыре атрибута: height, weight, name, age. Класс
# имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран.
# Создать объект класса Dog, вызвать всеметоды
# объекта и вывести на экран все его атрибуты.

# class Dog:
#
#     def __init__(self, name, age, height, weight):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight
#
#     def bark(self):
#         return f"{self.name} is barking on you!"
#
#     def run(self):
#         return f"{self.name} is barking to you!"
#
#     def jump(self):
#         return f"{self.name} is jumping on you!"
#
# bobik = Dog("Bobik",2,40,15)
#
# print(f"Name of the dog: {bobik.name}\nAge: {bobik.age}\nHeight: {bobik.height}\nWeight: {bobik.weight}")
# print(bobik.jump())
# print(bobik.run())
# print(bobik.bark())

# Hometask_14_2
# Добавить в класс Dog метод change_name.
# Метод принимает на вход новое имя и меняет атрибут имени у oбъекта. Создать один объект класса.
# Вывести имя. Вызвать метод change_name. Вывести имя.

class Dog:

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def change_name(self, new_name):
         self.name = new_name

#
#
bobik = Dog("Bobik",2,40,15)

print(f"The dog's name is {bobik.name}")
new_name = input("Enter the new name: ")
bobik.change_name(new_name)
print(f"The dog's name is {bobik.name}")