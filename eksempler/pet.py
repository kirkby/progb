class Pet:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def sound(self):
        pass

    def get_breed(self):
        print(f"{self.name} er en {self.breed}")

class Dog(Pet):
    sound = "vov"
    def __init__(self, name, breed, function):
        self.function = function
        super().__init__(name, breed)

    def sound(self):
        print(f"{self.name} siger {self.sound}!")


class Cat(Pet):
    def sound(self):
        print(f"{self.name} siger mjau!")
