# Afleveringsopgave
Programmering B, 2024-2025.  
Hold 2r.

Afsluttende aflevering for forløb 1.  
Individuel aflevering.  
Afleveres som pdf og evt. pythonprogram i lectio.   
Der må ikke benyttes AI. 


## Opgave 1
Betragt denne dette program: 

```python
vehicles = ["car", "mc", "bike", "scooter", "atv", "truck"]

def determine_vehicle(num_wheels, has_motor):

    if not has_motor and num_wheels == 2:
        return "bike"

    if has_motor and num_wheels == 2:
        return ["mc", "scooter"]

    if has_motor and num_wheels == 4:
        return ["car", "atv"]

    if has_motor and num_wheels > 4:
        return ["truck"]

vehicle = determine_vehicle(2, True)
space = " "
print("Possibilities: ", space.join(vehicle))
```
`join()` er funktion som sammensætter tekst til een streng. Den virker på lister og strenge.
Funktionen returnerer altså typen streng med den angivne separator, i dette tilfælde altså mellemrum. Separatoren kan dog være alle tegn, fx bindestreg. Eksempel:  
`"-".join(["1", "2", "3", "Go"])` &rarr; `1-2-3-Go`.

### 1.1
Lav en liste af alle variable i programmet. For hver variabel, angiv deres datatype.
Forklar kort med dine egne ord hvordan du bestemte variablernes datatype.

### 1.2
For hver af disse kald, angiv hvilken værdi og datatype som funktionen returnerer, hvis man kalder den med 
``` python
determine_vehicle(2, True)
determine_vehicle(3, True)
determine_vehicle(2, False)
```

### 1.3 
Virker alle eksemplerne i 1.2? Hvis ikke, hvordan kan man løse problemet?   
Fik du det svar som du forventede i alle tilfælde? Hvis ikke, hvorfor ikke?


## Opgave 2
``` python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
prime_numbers = [1, 2, 3, 5, 7, 11, 13]
print_primes = False

for item in numbers:
    if item in prime_numbers and not print_primes:
        print(item)
```

### 2.1
Hvad udskriver denne kode?

### 2.2
Hvad er `item` i dette eksempel? 
### 2.3
Hvilken slags struktur er `for-in`? 
Beskriv med egne ord mindst 2 andre strukturer af samme slags i Python.


## Opgave 3

### 3.1
Aflever en kommenteret udgave af jeres besvarelse af [opgave 7](https://github.com/kirkby/progb/blob/main/f1/opgaver.md#opgave-7).  
Kommenteret vil sige at I indsætter kommentarer i koden (med `#` fx) som  forklarer hvad koden gør.  
I skal også dokumentere funktionen med en _docstring_. 
Eksempel på docstring:
``` python
def calculate_age(date_birth):
    """Beregner en persons alder baseret på fødselsdato.

    Args:
      date_birth: Fødselsdato i formatet "YYYY-MM-DD".

    Returns:
      En persons alder som et heltal.
    """
```
I skal altså sørge for at funktionen altid kun returnerer _en_ (1, one, uno) VÆRDI, fordi svaret er entydigt. I er velkomne til at lave lige så meget om i programmet som nødvendigt. Fx behøver funktionen måske ikke at returnere en liste hvis der altid kun er _et_ svar? Skriv en kort redegørelse for jeres valg.

### 3.2 Bonusopgave (for dem der har tid og lyst)
Skriv en `pretty_print()` funktion som modtager returværdien fra jeres funktion og printer resultatet på en lækker måde.






