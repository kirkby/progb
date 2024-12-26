# Læreplan for Programmering B 
Med udgangspunkt i programmeringssproget python (v 3.1).

Se også [Studieplan](studieplan/0-studieplan.md).

## 1. Introduktion og opsætning
    1.1 Installation
    1.2 VS Code
    1.3 Syntaks i python
    1.4 Indrykning og blokke
        - significant whitespace
    1.5 Kommentarer
        - #
        - """
    1.6 Reserverede ord

## 2. Variable og simple datatyper
    2.1 Variable
        - navn og værdi
        - virkefelt (scope)
        - global
    2.2 Simple datatyper
        - heltal (integer)
        - kommatal (float)
        - tekst (streng, string)
        - sandt/falsk (boolean)

## 3. Kontrolstrukturer
    3.1 Betingelser
        - if
        - if-else
        - if-elif-else
    3.2 Gentagelser
        3.2.1 range()
        3.2.2 for-in
        3.2.3 while   

## 4. Nyttige funktioner
    4.1 Formatering af tekst: print(f"")
    4.2 Brugerinput: input()

## 5. Lister (arrays)
    5.1 Egenskaber ved de fire typer af lister
        - ordnet - uordnet
        - unikke - duplikerede elementer
        - uforanderlig (immutable) vs. foranderlig 
        - indeksbaseret - nøglebaseret - sæt
    5.2 Liste (List)
        ['item1', 'item2']
    5.3 Dictionary (opslagsliste, ordbog)
        {'key': 'value'} 
    5.4 Tupel (Tuple) 
        ('item1', 'item2')
    5.5 Sæt (Set)
        {'item1', 'item2'} (set)

## 6. Operationer på almindelig liste
    6.1 Gennemløb med for-in
    6.2 slicing [:]
    6.3 indeksering []
    6.4 append() og remove()
    6.5 Længde, sortering o.a.

## 7. Funktioner()
    7.1 built-in vs. user-defined
    7.2 global - virkefelt (scope)
    7.3 Parametre og argumenter
    7.4 Default-værdier
    7.5 Returværdier (return)
    7.6 Returværdien None
    7.7 Navngivne parametre
    7.8 Positionelle parametre
    7.9 Early return vs one exit point

## 8. Iterativ udvikling og programudvikling
    8.1 Den iterative udvklingsproces
    8.2 Design
        - rutediagrammer
        - pseudokode
    8.3 Implementation
    8.4 Test
    8.5 Fejlretning
    8.6 Vedligeholdelse
    8.7 Dokumentation

## 9. Standardbiblioteket PSL
    9.1 Populære standardmoduler
    9.1 import og from - import

## 10. Modularisering
    10.1 Modularisering
    10.2 Installation af moduler (libraries)
    10.3 Eksempel: datetime, random, requests
    10.4 Udvikling af egne moduler
    10.5 API'er

## 11. Forløb: Spil med pygame
    11.1 pygame
        - The Game Loop
        - Game Control
    11.2 Sprites


## 12. Advancerede begreber
    12.1 Funktioner og rekursion
    12.2 Polymorfi
    12.3 Algoritmemønstre
    12.4 Parametrisering/abstraktionsmekanismer
    12.5 Modularisering

## 13. Advanceret, kun i 3.g: Objektorienteret programmering
    13.1 Objekter
    13.2 Klasser
    13.3 "this"
    13.4 attributter
    13.5 metoder
==============================

# Tilrettelæggelse og didatik

Didaktiske principper:
- use-create-modify
- gradvise forbedringer (stepwise improvement)
- gennemprøvede eksempler (worked examples)
- faded guidence
- consume before produce

Worked examples arbejder med tutorials og vejledninger.

Stepwise improvement har tre dimensioner:
- konkretisering
- udvidelse
- omstrukturering

Tilrettelæggelse:
- overblik
- eksperimenter
- øvelser
- projekter

"Der veksles mellem overbliksskabende forløb, eksperimenter, øvelser, og projekter."

Det fremhæves at en programmør arbejder i iterative faser:
- design
- implementation
- test
- fejlretning
- vedligeholdelse

Begreber
- rekursion
- polymorfi
- algoritmemønstre
- parametrisering/abstraktionsmekanismer
- modularisering (moduler)

Redskaber og arbejdsgange
- test og fejlsøgning
- biblioteker og API'er
- dokumentation
- rutediagrammer
- pseudokode
- git (github)
- AI, kodehjælp