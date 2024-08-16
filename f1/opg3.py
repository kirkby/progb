""" demonstration af 
loops med range() 
loops med lister 
"""

for i in range(10):
  print(i)

for i in range(3, 13):
  print(i)

for i in range(25, 10, -2):
  print(i)

for i in range(0, 20, 2):
  print(i)

"""" Opgaver
- udskriv en liste af tal fra 1-50 - men kun de lige tal.
- udskriv en liste af tal fra 50-1 - men kun de ulige tal.

Brug cheatsheet eller google hvis I er i tvivl om syntaksen.
"""
for kodesprog in ('python', 'c#', 'html'):
  print(kodesprog)

for kodesprog in ('python', 'c#', 'html'):
  print(kodesprog.upper())

kodesprog = ('python', 'c#', 'html')
for i in range(3):
  print(kodesprog[i])

for kodesprog in ('python', 'c#', 'html'):
  # Vi vil kun have python
  if kodesprog == "Python":
    print(kodesprog)

# hov - hvorfor virker sidste eksempel ikke som forventet? 

"""" Opgaver
- udskriv en liste af tal fra 1-50 - sæt en stjerne ved siden af tallet hvis det er et primtal. Tip: brug liste med primtal
og if-blok og liste-funktionen "in"

"""
