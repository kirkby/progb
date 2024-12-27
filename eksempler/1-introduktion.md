 # Introduktion til Python

Programmering B
Hold 2.r
2024-25.

Vi bruger Python til at lære programmering.  
Python 3.1.12 er den nuværende version.

## Oversigt
Vi skal lære om:

- syntaks
- blokke
- simple datatyper som heltal, tekst og sand-falsk
- simple test som if, if-else og if-elif-else
- løkker (loops) med for-in, range()
- lister - som fx `[1, 2, 3]`
- funktioner

Vi skal bruge følgende værktøjer og programmer:

- en kodeeditor (IDE)
- en kommandolinje (CLI)
- Python 3

&#x24D8; **IDE** er et akronym for _Integrated Development Environment_. Altså, en kodeeditor, det program som vi skriver vores programmer i. Vi bruger VS Code som er en IDE fra Microsoft.

&#x24D8; **CLI** betyder *command line interface*, altså kommandolinjegrænseflade. 


### VS Code
Som en snedker har sit træværktøj, har du din kodeeditor. Brug tid på at lære den at kende!  Se fx [denne video](
https://code.visualstudio.com/docs/introvideos/productivity) med tips og tricks.
Eller [denne her](
https://code.visualstudio.com/docs/introvideos/configure) om temaer.

⚠️ Du bør som minimum kende genvejen <kbd>Space</kbd> + <kbd>Ctrl</kbd> + <kbd>P</kbd> (Mac: <kbd>Shift</kbd> + <kbd>&#x2318;</kbd> + <kbd>P</kbd>) - den giver direkte adgang til ALT hvad man kan i VS Code. Prøv den nu.

### Python CLI
Man kan arbejde med python på kommandolinjen på flere måder. 

#### Interactive mode

Hvis man skriver kommandoen `python3` i sit CLI, starter man python i _interactive mode_.
```
$>python3
Python 3.10.12 (main, Sep 11 2024, 15:47:36) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Derefter kan man "tale interaktivt med" python. _Interactive mode_ kan ses på at prompten er tre vinkler: `>>>`. 

For at afslutte "samtalen" skriv `quit()`.

#### Afvikling af python-kode i py.filer
Hvis man vil have python til at afvikle et program som man har gemt i en fil, skriver man 
```
python3 min-app.py
```
Her afvikler python programmet i filen `min-app.py` og stopper derefter.

En typisk fejl er at glemme om man befinder sig i _interactive mode_ eller udenfor.

## Syntaks
Python har en lidt speciel syntaks, sammenlignet med mange andre programmeringssprog. Det tilhører nemlig familien af sprog som anvender [_significant whitespace_](https://en.wikipedia.org/wiki/Off-side_rule). 

Dette er i modsætning til mange andre programmeringssprog som anvender bestemte tegn, fx krølleparenteser  `{}` (som også kaldes _Tuborg-klammer_}, til at adskille blokke.

### Indrykning
Python bruger udelukkende **indrykning** (_indentation_) til at afgrænse blokke af kode fra hinanden. 

For at definere en blok kode sætter man et kolon og rykker næste linje ind med **4 mellemrum**.
Alle linjer, der følger herefter og har samme indrykning, tilhører samme blok. 

``` python
1: x, y, swap = 10, 5, True
2: if swap:  # samme blok 2-5
3:     i = x 
4:     x = y 
5:     y = i 
6: i = 0 # anden blok
```
Hvorfor er det vigtigt om to linjer kode tilhører samme blok? Jo, fordi kode der tilhører samme blok, _altid eksekveres sammen_. Det er umuligt at læse og forstå kode, hvis man ikke forstår hvilke linjer der hører sammen i hvilke blokke.

Bemærk i øvrigt det afsluttende **kolon** `:` på første linje i blokken. Det har ingen anden funktion (så vidt vides) end at gøre det nemmere at læse - det betyder altså "her begynder en blok". Næste linje **skal** altså være indrykket, hvis linjen slutter med kolon.

Det samme gælder funktioner som også er en slag blokke. Sammenlign fx definitionen af en funktion i javascript

``` javascript
function greet(name) { 
    console.log("Hello, " + name + "!"); 
}
i = 10; // Tilhører ikke funktionen
```
med python
``` python
def greet(name): # kolon = her begynder blok
    print("Hello, " + name + "!") # 4 mellemrum, tilhører funktionen
i = 10 # Tilhører ikke funktionen 
```
VS Code sørger som regel for at indrykningen sker automatisk når man arbejder med `.py`-filer. 

Standarden med netop 4 mellemrum som indrykning er _best practice_. I virkeligheden er python ligeglad - sålænge linjerne har samme indrykning, hører de sammen. 

### Linjeskift
Tilsvarende er linjeskift også vigtige (syntaktisk signifikante) - hvilket også er forskelligt fra fx javascript og C#.
**I Python kan man afslutte et statement med et linjeskift** - uden semikolon. 

Linjeskift indikerer ny statement.
``` python
first_name = "Peter"
last_name = "Nielsen"
full_name = first_name + " " + last_name
```

Det samme kunne skrives med semikolon ...
``` python
first_name = "Peter"; last_name = "Nielsen"; full_name = first_name + " " + last_name
```
... men lad være med! Det er ikke _pythonic_ - det er altså imod ånden i python.

### Opsummering
Vi har i det foregående brugt begreberne linjer og blokke uden rigtigt at definere dem helt præcist. Hvis du ikke er helt sikker på, at du forstår disse begreber endnu, gør det ikke noget.   
Det vigtigste er, at du grundlæggende ved hvordan man skal forstå pythons særlige syntaks - altså ved hvordan man læser koden.


## Variabler
Hvad er en variabel? Vi kender dem måske fra matematik, når vi beregner resultat af en funktion.
```
y = f(x)
```
Her beregner vi funktionen af `x` og gemmer værdien som `y`.

i python skriver vi fx
``` python
school = "Slotshaven"
classname = "2r"
student_count = 11
htx = True
hhx = False
```

En variabel er altså "et navn med en værdi". Navnet kan ikke ændre sig. En variabel hedder altid det samme.
Hvis den hedder noget andet, er det en anden variabel. Værdien derimod - den kan ændre sig.

``` python
student_count = 11
print(student_count) // 11
student_count = 10 // Nogen er kommet for sent
print(student_count) // 10
```

Variabler har _datatyper_. Typer kan være simple eller komplekse. 
Vi begynder med de simple typer:

- streng (tekst)
- integer (heltal)
- boolean (sandt eller falsk)

De komplekse typer er fx lister af forskellig art, men det kommer vi til.

``` python
age = 11 # heltal (integer)
name = "Peter" # tekst (string) 
is_htx = True # sandt/falsk (boolean)
has_car = False # do.
```
Som programmør er det dog meget vigtigt at vide hvilken type en variabel har, da det har betydning for hvilke operationer som man kan udføre med variablen.

Man kan komme galt afsted hvis man ikke har styr på det.

``` python

# name er et heltal - hvilket er underligt men ok ...
name = 15
# men dette er ikke okay ...
name = name.capitalize() # ERROR!
# AttributeError: 'int' object has no attribute 'capitalize'
```
Man kan ikke gøre et heltal til et stort bogstav.

Men man må gerne skifte en variabel type - Python er ligeglad - men lad være med det.

``` python
name = 15 
name = 'anna' # nu er name faktisk et navn
name = name.capitalize() # Anna
```

&#x24D8; Datatyper er et MEGET vigtigt begreb i programmering, men det er også et meget stort emne så det vender vi tilbage til.


## Kontrolstruktur: if og if-else og if-elif-else

`if` og dens varianter er måske den mest basale alle såkaldte kontrolstrukturer - den bestemmer hvilken 
retning programmet skal løbe i. Det gør den ved at afgøre sandhedsværdien i en given test. 

``` python
name = "Peter"
if name == "Peter":
    print("Hej Peter") # Hej Peter
```
Testen afgører om variablen `name` er sat til "Peter" - hvilket jo enten sandt eller falsk.
Men hvad skal der ske hvis navnet ikke er "Peter"?
Så bruger man `else` - det bliver udført hvis testen evaluerer til falsk.


``` python
name = "Peter"
if name == "Peter":
    print("Hej Peter") # Hej Peter
else:
    print("Hej X") # Du hedder ikke Peter

```
`else` er altså det som sker, hvis alt andet er falsk - det er en slags default.  
Hvis der også er en Søren, kan man bruge "else-if" som i Python hedder `elif`.

``` python
name = "Henrik"
if name == "Peter":
    print("Hej Peter") # navnet er Peter
elif name == "Søren":
    print("Hej Søren") # navnet er Søren
else:
    print("Hej X") # Du hedder hverken Peter eller Søren

```
Nu har vi altså to tests og en default. Det ser sådan ud:

![If-elif-else](../images/if-elif-else.png)


Bemærk at rækkefølgen af tests har betydning. Betragt:

``` python
age = 19
if age > 18
    print("Du er gammel nok til kørekort") 
elif age > 90 # bliver aldrig sand - hvorfor?
    print("Du er for gammel til kørekort") 
else:
    print("Du er for ung til kørekort")
```
Tænk over hvorfor test 1 og 2 bør skifte rækkefølge.


## Loops

Funktionen [`range()`](https://docs.python.org/3.12/tutorial/controlflow.html#the-range-function) er et loop, altså en kontrolstruktur som udfører en løkke. 
Den gentager altså blokken der følger efter så mange gange som man beder den om. 
Antallet af gentagelser kaldes også _iterationer_. 

Den tager tre parametre - start, slut og hop (_increment_ eller _step_).
Men - hvis man bare vil tælle op et tal ad gangen, behøver man kun et parameter - nemlig slut-parameteret.
I det tilfælde er start lig med 0 og hop lig med 1 (første eksempel).
Det vil sige at funktionen har default-værdier for start og hop (nemlig 0 og 1), hvis man ikke angiver nogle værdier.

``` python
for i in range(10):
  print(i) # 0 1 2 3 osv. op til 9

for i in range(3, 13):
  print(i) # 3 4 5 osv op til 12

for i in range(0, 20, 2):
  print(i) # 0 2 4 6 .. op til 18

for i in range(25, 10, -2):
  print(i) # 25 23 21 19 17 15 13 11
```

> &#x24D8; What!? `range(10)` tæller fra 0 til 9! Bemærkede I det? Dataloger er underlige når de tæller - de begynder med 0. Lev med det indtil videre.

Konklusion: `range()`-funktionen er praktisk hvis man på forhånd kender antallet af iterationer eller skal bruge en liste af tal. 

Der er andre typer loops - men først kigger vi lige på lister.

## Lister
Lister er en helt grundlæggende datastruktur i programmering. I andre sprog kaldes de også _arrays_.

I python er der fire forskellige typer lister:
- liste (_list_)
- sæt (_set_)
- tupel (_tuple_)
- dictionaries

For nu koncenterer vi os om den første type og glemmer de andre et stykke tid.

Vi begynder med lister først. En liste kan kendes på sine kantede parenteser.
```
students = ['Peter', 'Anna', 'Pernille']
```


### Operationer på lister

Der er en række basale ting som ofte gerne vil gøre med en liste: tilføje, fjerne, opdele osv. 

Man kan tilføje elementer til en liste med `append()`.
``` python
students = ['Peter', 'Anna', 'Pernille'
students.append('Henrik') # tilføj Henrik
```

Man kan fjerne elementer til en liste med `remove()`.
``` python
students = ['Peter', 'Anna', 'Pernille'
students.remove('Peter') # fjern Peter
```

Man kan tilgå listens enkelte elementer via dets _indeks_. 
Indeks angives i kantede parenteser, altså `[]`.

Sådan finder man fx det første og sidste element i en liste.
``` python
students = ['Peter', 'Anna', 'Pernille']
first = students[0] # Peter
last = students[-1] # Pernille
```

En meget anvendt og kraftfuld på lister er _splice_, eller deling, af lister.
Hertil bruger man `[:]`, _the splice operator_. Den returnerer en _substring_, eller delstreng, af en liste.
Vi kan dele listen i drenge og piger således:
``` python
students = ['Peter', 'Anna', 'Pernille']
boys = students[0:1] # Peter
girls = students[1:2] # Anna Pernille
```

Forklaring på slice-operatoren:
> The slice operator [n:m] returns the part of the string starting with the character at index n and go up to but not including the character at index m.

I `[n:m]` refererer `n` og `m` altså til listens indeks. MEN - den begynder
med indeks `n` og tæller op til `m` _men tager ikke tegnet på indeks m med!_

Hvis man udelader et indeks, betyder det hhv. fra begyndelsen af listen eller til slutningen af listen.
Derfor får vi 
``` python
students = ['Peter', 'Anna', 'Pernille']
# Fra begyndelsen af listen til men ikke med indeks 1!
boys = students[:1] # Peter
# Fra indeks 1 til slutningen af listen
girls = students[1:] # Anna Pernille
```

Hvad skete der lige der? Dette er Python-magi. 
Man kan udrette meget med `[:]`.


En underlig ting er **kopiering** af lister - det gøres med den tomme parentes, således:
``` python
students = ['Peter', 'Anna', 'Pernille']
copy_of_student = students[:]
```

Længden af en liste findes med `len()`.
``` python
num_students = len(students)
```

Sortering sker med `sort()`.
``` python
students.sort()
```

Vi kan også vende den om.
``` python
students.reverse()
```

### Loops igen - nu med lister
Lad os kigge på loops igen - nu med lister. Vi looper igennem lister med strukturen `for-in`.

Den har formen `for X in LISTE:` hvor `for` og `in` er reserverede ord.
X er en variabel som får værdien af et nyt element i listen for hver gang vi gentager løkken.

``` python
for code in ['python', 'c#', 'html']:
  print(code) # python c# html

for code in ['python', 'c#', 'html']:
  # Vi vil kun have python
  if code == "Python":
    print(code) # python

code_languages = ['python', 'c#', 'html']
# Man kan også tælle sig igennem en liste via indeks.
for i in range(3):
  print(code_languages[i]) 
```

### test med lister

Ofte vil man gerne vide om en liste indeholder et bestemt element.
Det kan gøres nemt med `if` og `in`.

``` python
languages = ['python', 'c#', 'html']
if 'python' in languages:
  print('vi har python i vores liste!')

numbers = [1, 3, 5, 7, 9]
if 3 in numbers:
  print('3 fundet') 

```

## Reserverede ord
Programmeringssprog har _reserverede ord_. Det er ord som programmøren ikke må bruge som variabelnavne. 

Andre reserverede ord i Python er fx
``` python
for in if elif else True False
```

I Python må man ikke kalde sin liste for `list`. Kan I regne ud hvorfor? 

&#x261E; Det er en datatype.

## Funktioner 
Som I måske har bemærket, bliver et program meget hurtigt uoverskueligt. Det er tid til at modularisere det.
Det kan man gøre på flere måder, men vi begynder med at opdele vores kode i _funktioner_. 

Der er en række ting at sige om en funktion så hold nu fast: 
 - Man kan altid kende en funktion på parenteserne - `funktion()`. 
 - En funktion har eller kan have parametre.
 - En funktion har en returværdi. 
 - En funktion definerer sit eget virkefelt (_scope_) (det vender vi tilbage til)).

Uden at vide det, har vi allerede brugt funktioner - nemlig Pythons indbyggede funktioner som fx `print()`.
Man skelner altså Pythons _egne_ funktioner - de såkaldte [_built-in functions_](https://docs.python.org/3/library/functions.html) - og de funktioner som man selv definerer.

En funktion erklærer man i python med det reserverede ord `def`.
``` python
def add_item_to_grocery_list(item):
  grocery_list.append(item)
```  
Det er som vi kender det fra Python - alt hvad der følger efter kolon (`:`) og er _indrykket_ under funktionen, er kode som tilhører funktionen. 

Variablen `item` i ovenstående eksempel kaldes et parameter. Det er den data som man giver til funktionen.  
Husk at funktion en funktion kan kendes ved `()` - så de skal med, selv om funktion ikke har parametre.

``` python
from datetime import date

def print_date():
    """ Denne funktion har ingen parametre """
    today = date.today()
    print("Today's date:", today)
```  

Funktioner er den vigtigste byggesten i programmering. Man bruger først og fremmest funktioner til "pakke kode ind" som
skal løse små, afgrænsede problemer igen og igen. 

Næste vigtige punkt er at man kan _generalisere_ løsningen på et problem ved hjælp af funktioner.
Hvis man fx har en mail-funktion, kan man fx bruge email-adresse som parameter. 

``` python
def send_welcome_mail(mail):
    """ Denne funktion sender en velkomst mail """
    # send welcome mail til "mail".
```  
I dette tilfælde har man lavet en `generel` funktion som kan sende velkomst-mails til en mail-adresse fordi man kan angive mail-adressen som et parameter til funktionen.

Denne kode printer Fibonacci-tal op til 100.
``` python
a, b = 0, 1
while a < 100:
    print(a, end=' ')
    a, b = b, a+b
```  
Men hvorfor lige tallet 100? Det er et helt tilfældigt tal. Hvorfor ikke gøre 100 til et parameter og lave en generel funktion? Lad os udskifte 100 med et parameter ved navn `limit`.

``` python
def fib(limit):
    a, b = 0, 1
    while a < limit:
        print(a, end=' ')
        a, b = b, a+b
    print()
```

Kør denne funktion i VS Code. Men hov - den gør jo ikke noget. 

Hmm, en funktion skal kaldes.

``` python
fib(25) # calling fib()
# 0 1 1 2 3 5 8 13 21 
```

Funktioner anvendes som sagt til afgrænsede, enkeltstående opgaver.
Nogle kloge folk siger, at som udgangspunkt skal man kunne overskue hele funktionen i et skærmbillede. 


### Mere om parametre
En funktion kan selvfølgelig have mere end et parameter. Faktisk kan en funktion have et stort set uendeligt antal parametre. 

Der er en dog en tommelfingerregel som  siger at hvis en funktion har flere end 3-4 parametre, så skal man overveje om ens funktion er for indviklet. 



``` python
def say_hello(greeting, title, name):
    print(greeting, title, name)

say_hello('Hej', 'hr.', 'Jensen') # Hej hr. Jensen
say_hello('Goddag', 'fru', 'Hansen') # Goddag fru Hansen
say_hello('Hva så', 'der, ', 'mester') # Hva så der, mester

```

Dette eksempel kan synes lidt fjollet. Men denne funktion kunne faktisk være meget smart, hcis man senere besluttede sig for at ændre på den måde som man hilser på. Så ville man kun skulle ændre koden et sted. Vi kan fx gøre brug af Pythons indbyggede formateringsmuligheder:

``` python
def say_hello(greeting, title, name):
    print(f"Sig {greeting} til {title} {name}") # Sig Hej til hr. Jensen
```

Udover parametre taler man også om _argumenter_. 

Et _argument_ er den værdi som man _kalder_ funktionen med - altså de konkrete værdier som parametrene får når funktionen kaldes.

I eksemplet ovenfor er parametrene altså `greeting`, `title`, `name` - og "Hej", "hr.", "Jensen" de tre argumenter som funktionen bliver kaldt med.

### Default-værdier
Noget mere interessant er måske default-værdier for parametre.

``` python
def animals_greeting(greeting, first_animal = "cat", second_animal = "dog"):
    print(f"The {first_animal} says {greeting} to the {second_animal}.")

animals_greeting("hello", "bird", "mouse")
# men også
animals_greeting("hello") # The cat says hello to the dog
```
Igen er rækkefølgen vigtig: Reglen er at parametre med default-værdier skal komme efter parametre uden default-værdier.

Dette går ikke:
```python
def animals_greeting(first_animal = "cat", second_animal, greeting):
    # ( ... )

SyntaxError: parameter without a default follows parameter with a default
```

Default-værdier giver mening hvis man _næsten altid_ kalder en funktion med de samme værdier - hermed fortæller man at visse værdier er normaltilfældet.

``` python
def print_document(document, all_pages = True, use_duplex = True):
    """ By default, prints full doc as duplex """
    # Print your document here


print_document(document) # using default values for 2nd and 3rd argument
```
Det betyder, at man i de fleste tilfælde kan udelade andet og tredje argument, hvis man bare ønsker at printe _hele_ dokumentet som _duplex_.

Når kalder bruger `return` så forlader eksekveringen funktionen og vender tilbage til kaldet.


### Returværdier
En funktion kan returnere en værdi med `return`-nøgleordet.

``` python
def calculate_age(date_of_birth):
    """ Calculates and returns age by comparing current date with date_of_birth """
    # Do the calculation
    return age
```

#### Returværdien None

``` python
def pretty_print(message):
    """ Pretty prints message """
    print(f"Message: {message}")

return_value = pretty_print("This is Public Service Announcement")

print(f"Returværdi: {return_value}")
--
Returværdi: None
```


#### Multiple returns
Man kan sagtens "returnere" flere gange i samme funktion.

``` python
def determine_vehicle(num_wheels, has_motor):

    if not has_motor and num_wheel == 2:
        return ["bike"]

    if has_motor and num_wheel == 2:
        return ["mc", "scooter"]

    if has_motor and num_wheel == 4:
        return ["car", "atv"]

    if has_motor and num_wheel > 4:
        return ["truck"]
```


I dette eksempel returnerer vi en værdi ligeså snart vi har fundet den. Det kaldes _early return_. 
Princippet er at man finder de nemmeste løsninger først og dermed reducerer kompleksiteten i antallet af kombinationer.
Fordelen ved dette er at man kan holde funktionen simpel - man behøver ikke så mange betingelser og indrykninger.

Der findes en modsat skole - _one exit only_ - som mener at man kun skal returnere en gang til sidst i funktionen. 

Sammenlign disse eksempler:

Early return
``` python
if (condition)
   return 42;
else
   return 97;
```

"One exit point"
``` python
int result;
if (condition)
   result = 42;
else
   result = 97;
return result;
```

Se også [denne tråd på StackExchange](https://softwareengineering.stackexchange.com/questions/118703/where-did-the-notion-of-one-return-only-come-from).


Jeg foretrækker den første løsning.

&#x24D8; Dokumentation af funktioner


En 1-linjes tekst lige under funktionshovedet, fx kunne vores fibonacci-funktion dokumenteres sådan her: 

``` python
def fib(limit):
    """Print a Fibonacci series up to limit."""
    a, b = 0, 1
    (...)
```


## Standardbiblioteket
Python bliver leveret med et [standardbibliotek](https://docs.python.org/3/library/index.html).
Standardbiblioteket er altid tilgængeligt i python.

Lad os se på et par stykker.

``` python
os: For interacting with the operating system.
sys: For accessing system-specific parameters and functions.
math: For mathematical operations, such as trigonometry and logarithms.
random: For generating random numbers and sequences.
datetime: For working with dates and times.
json: For encoding and decoding JSON data.
```

Alle disse biblioteker eller _moduler_ indeholder nyttige funktioner, som man ofte har brug for.

Så hvis vi fx har brug for et tilfældigt tal, så importerer vi `random` - og det gør man altid som det første. Det vil sige at man begynder filen med sine `import`-statements.
``` python
import random # hent tilfældighedsmodulet

coin_sides = ['plat', 'krone']
result = random.choice(coin_sides) # random.choice() giver tilfældig side
print(result)
```

Et andet rigtig godt eksempel er tid og dato. 

For at få adgang til de indbyggede tid- og datofunktioner _importerer_ man `datetime`. 

``` python
import datetime # importer Pythons tidsbibliotek

# datetime har en række funktioner, 
# fx tiden lige nu ...
now = datetime.datetime.now()
print("Current time:", now) # Current time: 2024-09-10 06:59:26.537157

# eller dagens dato
today = datetime.date.today()
print("Today's date:", today) # Today's date: 2024-09-10
```
 Man kan også oprette sine egne datoer eller tidspunkter.
``` python
# Opret en dato
specific_date = datetime.date(2024, 11, 24)
print("My specific date:", specific_date)

# Opret et tidspunkt
specific_time = datetime.time(13, 30, 0)
print("My specific time:", specific_time)
```

Med modulet `os` (Operating System) kan man få fat i filsystemet, altså de omgivelser som Python lever i på computeren. Vi kunne godt tænke os at læse data fra en fil - så skal vi bruge `import os`.

``` python
import os

with open("data.txt", 'r') as f:
    contents = f.read()
    print(contents)
```
Prøv det på din egen maskine.

Eller hvad med en liste af alle filer i den mappe som vi befinder os i?
``` python
import os

directory = os.getcwd()
for item in os.listdir(directory):
    if os.path.isdir(item):
      print(f"{item} (directory)")
    else:
      print(f"{item} (file)")
```
Prøv det på din egen maskine. 

### Import af egne moduler
Man kan også importere sine egne moduler. I store programmer vil man ofte opdele koden i flere filer som man så importerer i sit hovedprogram. Hvis man gerne vil bruge sin indkøbsliste-kode, kan man importere en fil således:
```
import grocery-list
```
Det er nemt nok. 


Men hvad hvis den funktionalitet som man skal bruge ikke findes i pythons standardmoduler? Det kigger vi på nu.

### Eksterne moduler
De fleste moduler skal man dog selv installere før man kan bruge dem. Disse moduler henter man i [PYPI](https://pypi.org/) - The Python Package Index. 

Lad os tage et eksempel - hvad med internettet? Kan man ikke få fat i det? Lad os se om der er et modul til det.

Et meget populært modul til at lave http-forespørgsler er `requests`.
Se https://pypi.org/project/requests/.

``` python
import requests

url = "https://api.dataforsyningen.dk/adgangsadresser"
params= {"vejnavn": "Slotshaven", "husnr": "1", "struktur": "mini"}
data = requests.get(url, params).json()
for item in data:
    for key, value in item.items():
        if (key == 'betegnelse'):
            print("Adresse: ",  value) 

# Adresse:  Slotshaven 1, 4200 Slagelse
# Adresse:  Slotshaven 1, 4300 Holbæk
```
Vi har netop stillet en forespørgsel til Danmarks offentlige data og fået et svar. Læs mere hos [dataforsyningen.dk](https://dawadocs.dataforsyningen.dk/dok/api/adgangsadresse#s%C3%B8gning). Der er åbenbart også en Slotshaven i Slagelse _of all places_.

Men før det virker, skal man først installere modulet `requests`. Det er ikke et af standardmodulene - så hvor kom det modul fra? 
Det installerer vi fra 