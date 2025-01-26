### Introduktion til klasser og objekt-orienteret programmering i Python

Objekt-orienteret programmering (OOP) er en populær måde at strukturere og skrive programmer på. I OOP organiserer vi vores kode omkring "objekter", som kan repræsentere ting fra den virkelige verden, som fx en bil, en person eller et kæledyr. Hvert objekt tilhører en "klasse", som er en skabelon for, hvordan objektet fungerer.

### Hvad er klasser og objekter?
En klasse er en skabelon eller model, som beskriver, hvordan objekter skal se ud og opføre sig. Et objekt er en konkret instans af en klasse. For eksempel kan vi have en klasse kaldet `Pet` (kæledyr), og hvert enkelt kæledyr, som vi opretter, vil være et objekt af typen `Pet`.

#### Eksempel på en klasse og et objekt
```python
class Pet:
    """
    En klasse, der beskriver et kæledyr.
    """
    def __init__(self, name, age):
        self.name = name  # Instansvariabel
        self.age = age    # Instansvariabel

# Opret en instans af klassen Pet
my_pet = Pet("Buddy", 3)
print(my_pet.name)  # Output: Buddy
print(my_pet.age)   # Output: 3
```

### Constructoren `init`
Constructoren er en speciel metode i Python, der kaldes, når vi opretter et nyt objekt fra en klasse. Den bruges til at sætte startværdier for objektets attributter. I eksemplet ovenfor initialiserer `__init__` attributterne `name` og `age`.

#### Eksempel med en constructor
```python
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Opret en instans
pet = Pet("Bella", 5)
print(pet.name)  # Output: Bella
print(pet.age)   # Output: 5
```

### Hvad betyder `self`?
`self` bruges i metoder til at referere til det aktuelle objekt, som metoden kaldes på. Det gør det muligt for hvert objekt at holde styr på sine egne data. Alle instansmetoder skal have `self` som deres første parameter.

#### Eksempel på brug af `self`
```python
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f"{self.name} er {self.age} år gammel."

pet = Pet("Charlie", 4)
print(pet.describe())  # Output: Charlie er 4 år gammel.
```

### Dunder
`__init__` er en såkaldt double underscore-metode - bedre kendt som *dunder* metoder. Dem findes der mange af.

```python
print(d.__dict__)

# {'breed': 'Golden Retriever', 'dog_type': 'familiehund', 'name': 'Fido', 'age': 2, 'random_attribute': 'Dette er en tilfældig attribut'}
```

### Subklasser og nedarvning
Med subklasser kan vi genbruge og udvide funktionaliteten af en eksisterende klasse. Subklasser nedarver alle attributter og metoder fra superklassen.

#### Eksempel på en superklasse og subklasser
```python
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "Kæledyret laver en lyd."

class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Kald superklassens constructor
        self.breed = breed

    def speak(self):
        return "Vuf!"

class Cat(Pet):
    def speak(self):
        return "Mijav!"

# Opret objekter af subklasser
dog = Dog("Max", 6, "Labrador")
cat = Cat("Whiskers", 3)

print(dog.speak())  # Output: Vuf!
print(cat.speak())  # Output: Mijav!
```

### Overrides af funktioner
Når en metode i en subklasse har samme navn som en metode i superklassen, vil subklassens version blive brugt. Dette kaldes at override en funktion.

#### Eksempel på override
```python
class Pet:
    def speak(self):
        return "Kæledyret laver en lyd."

class Dog(Pet):
    def speak(self):
        return "Vuf!"

pet = Pet()
dog = Dog()

print(pet.speak())  # Output: Kæledyret laver en lyd.
print(dog.speak())  # Output: Vuf!
```

### Opsummering
- En **klasse** er en skabelon for, hvordan objekter skal se ud og opføre sig.
- Et **objekt** er en konkret instans af en klasse.
- **Constructoren** `__init__` bruges til at initialisere objektets data.
- **`self`** refererer til det aktuelle objekt og bruges til at holde styr på dets data.
- **Subklasser** tillader genbrug og udvidelse af funktionalitet fra en superklasse.
- **Overrides** giver mulighed for at tilpasse funktionaliteten i subklasser.



## Materialer
**Dave Ebbelaar**
God introduktion på github: https://github.com/daveebbelaar/ai-fundamentals/blob/main/classes/README.md

Video: https://www.youtube.com/watch?v=u4Ryk0YuW6A  