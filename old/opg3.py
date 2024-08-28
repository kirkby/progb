""" demonstration af 
loops med lister 
"""
students = ['Peter', 'Anna', 'Pernille']

"""" Opgave til lister
Opret en liste med elever.
- udskriv denne liste
- tilføj 3 nye elever - find selv på navnene, sæt drengenavnene først
- udskriv listen baglæns
- udskriv alle navne i listen med store bogstaver
- opret en ny liste der indeholder alle drengenavne og pigenavne med splice operatoren
- udskriv alle navne fra indeks 2-5
"""


""" demonstration af 
loops med range()
"""
for i in range(10):
  print(i)

for i in range(3, 13):
  print(i)

for i in range(25, 10, -2):
  print(i)

for i in range(0, 20, 2):
  print(i)

# %%
# alle tal til og med halvtreds som kan divideres med 5.
for i in range(50):
  if i % 5 == 0:
    print(i, " kan divideres med 5")

# Der er en fejl i ovenstående - kan I se den? 
"""" Opgave til range()
- udskriv en liste af tal fra 1-50 - men kun de lige tal.
- udskriv en liste af tal fra 50-1 - men kun de ulige tal.
- udskriv alle tal fra 1-50 men sæt en stjerne ved tallet hvis det er et primtal. Tip: definer en liste af primtal og test med den.

Brug cheatsheet eller google hvis I er i tvivl om syntaksen.
"""

