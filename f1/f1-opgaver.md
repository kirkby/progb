
# Opgaver f1
Opgaver til forløb 1: Introduktion til Python

## Opgave 1: betingelser

Opgaver til 
- (a) if: 
- (b) blokke (hvad hører sammen), 
- (c) indrykning

(a) if: 
(b) if: else:
(c) if: elif: else: """

``` python
x = 1 
y = 2 
if x == 1:
  print('kat')
  if y == 2:
    print('hund')
  print('hest')
  if y == x:
    print('kanin')
print('dyr')
```
### Opgave 1A
Svar uden at køre programmet - hvad udskriver dette program? 
### Opgave 1B
Ret en variabel i programmet så det skriver hund - hest - kanin - dyr
### Opgave 1C
Giv en af variablerne en ny værdi så programmet skriver kat - hund - hest - kanin - dyr 
Tip: indsæt en  linje

## Opgave 2 Betingelse elif

``` python
age  = 100
if age > 18:
  print('Du kan tage kørekort')
else: 
   print('Du er ikke gammel nok til at tage kørekort') 
```

### Opgave 2A 
Indsæt en `elif:` betingelse som siger at hvis man er ældre end 100 år, er man for gammel til at tage kørekort.

### Opgave 2A 
Afprøv dit program. Virker det? Hvorfor er rækkefølgen af betingelserne vigtig?

### Opgave 2C
Indlæs alder fra kommandolinjen så programmet begynder med at spørge om ens alder.
Tip: brug `age = input()`


## Opgave 3 Loops og lister
```
students = ['Peter', 'Anna', 'Pernille', 'Tyra']
students.append('Søren')
students.remove('Anna')
for name in students:
    print(name)
```
Kør eksemplet og se hvad det udskriver.
### Opgave 3A
Tilføj 3 nye elever med `append()` og udskriv listen.
### Opgave 3B
Udskriv alle navne med STORE bogstaver - brug `upper()`
### Opgave 3C
Kopíer kun elementerne Anna og Tyra fra listen og udskriv listen (brug splice operatoren `[:]`)

## Opgave 4 range()
```
magic_numbers = [10]
for i in range(0, 20, 2):
  print(i, end = '-')
  if i in magic_numbers:
    print()
    print('10 is the magic number')
```
### Opgave 4A
Udskriv alle tal til og med halvtreds som kan divideres med 5.
### Opgave 4A
Udskriv en liste af tal fra 1-50 - men kun de lige tal.
### Opgave 4C
Udskriv en liste af tal fra 50-1 - men kun de ulige tal.
### Opgave 4D
Udskriv alle tal fra 1-50 men sæt en stjerne ved tallet hvis det er et primtal. Tip: definer en liste af primtal og test med den.






