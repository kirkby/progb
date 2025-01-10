class Pet:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def sound(self):
        pass

    def get_breed(self):
        print(f"{self.name} er en {self.breed}")

    # def get_pet(self):
    #     print(f"{self.name} er en {self.id
    # def get_pet(self):
    #     print(f"{self.name} er en {self.id}")


class Dog(Pet):
    id = "dog"

    def sound(self):
        print(f"{self.name} siger vov!")


class Cat(Pet):
    id = "cat"

    def sound(self):
        print(f"{self.name} siger mjau!")
