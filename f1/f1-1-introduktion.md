# Velkommen til programmering B!

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
