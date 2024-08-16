# Velkommen til programmering B !!!

Vi bruger Python til at lære programmering.  
Python 3.1.12 er den nuværende version.

## Forløb 1: Oversigt
Vi skal lære om:

- indrykning (indentation)
- blokke (blocks)
- kontrolstrukturer ()
- løkker (loops)

Vi skal bruge følgende værktøjer:

- en kodeeditor (IDE)
- en kommandolinje (CLI)

### IDE
IDE er et akronym for Integrated Development Environment. Altså, en kodeeditor, det program som vi skriver vores programmer i.
Vi bruger VS Code som er en IDE fra Microsoft.

### CLI
CLI betyder *command line interface* og er et andet meget brugt TLA..

(Joke: IT-verdenen er fuld af akronymer - der er så mange at man har opfundet begrebet TLA = Three Letter Acronym.)


Det betyder at man skriver kommandoer på en kommandolinjen. 
Eksempel: når vi skriver 

~~~
>python3 main.py
~~~

så arbejder vi med Python i CLI.

De tegn som står i begyndelsen af linjen, fx `>>>`, kaldes i øvrigt en prompt. 

Man kan konfigurere sin prompt så den ser ud som man ønsker. Fx kan den vise klokken eller eller ens brugernavn. 

### Python CLI
Hvis man skriver 
```
python3
```
i sit CLI, starter man python og kan derefter "tale med" python. 
Det kan se på prompten som ser sådan ud: `>>>`.

For at afslutte "samtalen" skriv `quit()`.

Hvis man vil have python til at afvikle et program som man har gemt i en fil, skriver man 
```
python3 mit-program.py
```
Her afvikler python programmet i filen og stopper derefter.
En typisk fejl er at glemme om man befinder sig "inde i python" eller udenfor.

### if og if - else og if elif else
![If-elif-else](https://images.ctfassets.net/wp1lcwdav1p1/3fr1rXjNZpGvfNtcL1uSo6/bbfd296116c1ed779f7aff0434d536a0/Elif_statement.png)

### Variable
Hvad er en variabel? Vi kender dem måske fra matematik, når vi beregner resultat af en funktion.
```
y = f(x)
```
Her giver vi y værdien af en funktion som får værdien x som inddata.

i python skriver vi fx
```
skole = "Slotshaven"
klasse = "2r"
elev_antal = 11
htx = True
hhx = False
```

En variabel er altså "et navn med en værdi". Navnet kan ikke ændre sig. En variabel hedder altid det samme.
Hvis den hedder noget andet, er det en anden variabel. Værdien derimod - den er kan ændre sig.

```
elev_antal = 11
print(elev_antal) // skriver 11
elev_antal = 10 // Nogen er kommet for sent
print(elev_antal) // skriver 10
```

Variable har typer. Typer kan være simple eller komplekse. 
Vi begynder med simple typer:

- streng (tekst)
- integer (heltal)
- boolean (sandt eller falsk)

De komplekse typer er primært lister af forskellig art. 

Eksempel på liste
```
elever = ['anna', 'peter', 'michael', 'sofie']
```

Det er meget vigtigt at vide hvilken type en variabel har, da det har betydning for
hvilke operationer som man kan udføre med variablen.

```
# streng - ok
navn = 'anna'
navn = navn.capitalize() # Anna

# heltal - ikke ok
navn = 15
navn = navn.capitalize() # ERROR!
# AttributeError: 'int' object has no attribute 'capitalize'
```

### Loops med range()
```
for i in range(10):
  print(i)

for i in range(3, 13):
  print(i)

for i in range(25, 10, -2):
  print(i)

for i in range(0, 20, 2):
  print(i)
```

Find tekst med nem gennemgang af Python for begyndere.