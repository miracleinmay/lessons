# Hometask_14_5
# Создать три класса: Dog, Cat, Parrot. Атрибуты каждого класса: name, age, master.
# Каждый класс содержит конструктор и методы: run, jump, birthday(увеличивает age на 1), sleep.
# Класс Parrot имеет дополнительный метод fly, Cat - meow, Dog - bark.

# Hometask_14_6
# Создать родительский класс Pet, содержащий все общие методы классов
# Dog, Cat, Parrot. Унаследовать Dog, Cat, Parrot от класса Pet. Удалить в
# дочерних классах те методы, которые имеются у родительского класса.
# Создать объект каждого класса и вызвать все его методы

class Pet:

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        return f"{self.name} is running!"

    def jump(self):
        return f"{self.name} is jumping!"

    def sleep(self):
        return f"{self.name} is sleeping!"

    def birthday(self):
        self.age += 1
        return f"{self.name} has birthday today! It is {self.age} today."


class Dog(Pet):

    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def bark(self):
        return f"{self.name} is barking!"


class Cat(Pet):

    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def meow(self):
        return f"{self.name} is meowing!"


class Parrot(Pet):

    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def fly(self):
        return f"{self.name} is flying!"


puppy = Dog("Bobik", 5, "Vasya")
print(puppy.__dict__)
print(puppy.bark())
print(puppy.birthday())
print(puppy.sleep())
print(puppy.jump())
print(puppy.run())

kitty = Cat("Belok", 4, "Eduard")
print(kitty.__dict__)
print(kitty.meow())
print(kitty.birthday())
print(kitty.sleep())
print(kitty.jump())
print(kitty.run())

budgie = Parrot("Kesha", 6, "Lily")
print(budgie.__dict__)
print(budgie.fly())
print(budgie.birthday())
print(budgie.sleep())
print(budgie.jump())
print(budgie.run())


