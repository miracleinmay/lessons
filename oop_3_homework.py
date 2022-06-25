# Hometask_14_8
# Добавьте в класс Pet дескриптор, чтобы нельзя было задать
# отрицательный возраст или 0


# Hometask_14_9
# Добавьте в класс Pet валидацию,
# чтобы у питомца было имя и хозяин

class PositiveAge:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, age):
        if age <= 0:
            raise ValueError("The age must pe a positive number!")
        instance.__dict__[self.name] = age

class NameisString:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, name):
        if name.isalpha():
            instance.__dict__[self.name] = name
        else:
            raise AttributeError("The name must be a string!")

class Pet:
    name = NameisString()
    age = PositiveAge()
    master = NameisString
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

lyolik = Pet("Lyolik", -12, "Sana")
print(lyolik.__dict__)
bobik = Pet("dkw24", 651, "Mina")
print(bobik.__dict__)

