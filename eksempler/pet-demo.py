from eksempler.pet import Pet, Dog, Cat

# import dog
dog = Dog("Fido", "Golden Retriever")
dog.sound()
dog.get_breed()
dog.breed = "gravhund"
dog.get_breed()
# dog.get_pet()

cat = Cat("Spot", "Perser")
cat.get_breed()
cat.sound()
print(" cat er en ", type(cat))

# weird
pet = Pet("Fido", "Golden Retriever")
pet.get_breed()
# pet.get_pet()
# print(" pet er en ", type(pet))
