# Git og GitHub
## Git
I disse moduler bliver du introduceret til et helt centralt samarbejdsredskab indenfor software udvikling: git. Git er et værktøj til source control. Når man programmerer og laver større it-projekter i det hele taget, er det supervigtigt at have styr på hvilke ændringer i koden der er lavet i hvilken rækkefølge, og af hvem. Det skal være muligt at gå tilbage til tidligere versioner, hvis noget viser sig at være forkert, og man skal sikre sig at de rettelser man laver ikke bliver overskrevet af andre, der også arbejder på projektet og som arbejder på andre dele af koden. Git er altså et versionsstyringsredskab, og et sådant ud over det sædvanlige.

## Grundprincipper og sprogbrug
Grundprincippet i git er, at man har et repository – i daglig tale et repo – som overvåges af git. Alle ændringer registreres i rækkefølge og efter hvem der laver dem. Man arbejder på filerne som normalt, og retter og gemmer undervejs, men når man på et tidspunkt er færdig, så fortæller man git, at “her er noget du skal huske” – man committer ændringerne til git (og man committer sig til ændringerne). Nu laver git en note om hvem og hvornår, samt en liste over forskellene mellem den gamle og den nye version.

## Github
Det smarte med git er i virkeligheden at bruge det sammen med GitHub . Mens git kan holde styr på mapper og filer lokalt på din computer, tager GitHub funktionaliteten ud på nettet. Du kan tænke på GitHub som en slags dropbox for programmører. Men I kan ikke kun dele jeres filer i skyen. Med git og GitHub har I fuld kontrol over hvem der retter og ændrer dem, hvornår de gør det og ikke mindst hvorfor. Og I er sikre på, at hvis der er konflikt mellem ændringsforslag, så bliver det opdaget – I kommer ikke til at slette hinandens arbejde ved et uheld.
Når man bruger GitHub, har man sit repo på nettet, på en GitHub-konto. Det kaldes origin eller remote, mens den mappe lokalt på maskinen, som man arbejder i, kaldes local. Git holder styr på, om filerne i den lokale mappe er identiske med origin eller om de er forud eller bagud for rettelser på GitHub. 

## Push og Pull
Det man arbejder på er i reglen filerne i den lokale mappe. Der hekser man rundt, retter og prøver sig frem, indtil man er tilfreds. Imens gemmer man hele tiden mellemresultaterne – men de skal jo ikke op til andre. Først når man har noget, der virker tilstrækkelig godt, vil man have nye filer og ændringer lagt op. Så laver man et commit, og skriver samtidig en lille note om, hvad det er for en ændring. GitHub noterer, at disse filer skal lægges op på origin. Man siger, at ændringerne er staged – altså sat i scene, lagt til rette for at blive uploaded.
Når du har rodet med dit repo lokalt og staged dine forbedringer, og derpå vil lægge det hele ud til andre på GitHub.com, kaldes det at pushe. Der er altså generelt tre trin i den samlede proces, og i konsollen ville det se således ud:
```
git add --all   // Læg eventuelle nye filer ind i projektet
git commit --all -m"Jeg har gjort dit og dat"   // stage
git push   // Læg filerne ud på GitHub
````

Eftersom GitHub ligger på nettet, er det ofte sådan at nogle andre har modificeret koden, eller du har måske selv arbejdet med den på en anden computer. Derfor er det ofte en god idé at starte med et pull, hver gang du starter, før du arbejder videre lokalt. På den måde er du sikker på dine lokale filer svarer til filerne på GitHub. 

## Lidt mere lingo
Et repo er en mappe hvor git holder øje med ændringer
At committe er at fortælle git, at nu er man klar med sine rettelser, og git skal føje dem til projektet
At forke er at kopiere en andens projekt ind i din egen konto på GitHub
At clone er at kopiere et projekt fra GitHub ned på sin egen computer
At fetche er at hente forandringer – men UDEN at ændre dine filer lokalt
En branch er en udgave af et repo der er blevet clonet lokalt
En remote branch er dette repo når den ligger på GitHub (kendes lokalt som origin)
At merge er at flette en branch ind i en anden
En konflikt er når man vil pulle noget ned, som ikke svarer til det man har lokalt, og hvor der er modsat rettede ændringer i de samme kodelinjer
