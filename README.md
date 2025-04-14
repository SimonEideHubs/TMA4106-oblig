# TMA4106-oblig
Standardprosjekt for oblig i TMA4106 fordi jeg er travel.

All kode som hører til en oppgave ligger i python-fila med tilsvarende navn.

## oppgaver 1-3: enkle estimeringer av e^1.5

### Oppgave 1

Denne metoden bruker bare et steg frem til å estimere den nåværende verdien. Derfor vil den nesten utelukkende (Foruten nærværet av andre feil) estimere for høyt for en funskjon som e^x. Dette er fordi den førstederiverte av e^x stiger monotont (Og såklart er e^x i seg selv).
Observerer slik det er forventet at presisjonen starter ganske dårlig til å begynne med, men blir bedre i proporsjon med steglengden. dette fortsetter frem til steglengden 10e-8 der estimated er nærmest den analytiske verdien ned til de 16 desimalene python jobber med her. Deretter stiger feilen igjen, siden avrundingsfeilen bare blir større og større. Dette synes litt i det føeste bildet, som viser estimat sammenliknet med forventer verdi, men best i andre figur som viser feil på logaritmisk skala.
![alt text](https://github.com/SimonEideHubs/TMA4106-oblig/blob/master/oppg1_1.png?raw=true)
Siden feilen fort blir veldig liten relativt til verdiene, blir denne grafen fort lite hjelpsom. Neste viser heller avvik fra forventet verdi (Med 16 desimalers presisjon) på logaritmisk skala. Her ser vi at feilen faller omtrent med en størrelsesorden for hver størrelsesorden i steglengden. Dette stemmer godt med at dette er en førsteordens estimering.
![alt text](https://github.com/SimonEideHubs/TMA4106-oblig/blob/master/oppg1_2.png?raw=true)


### Oppgave 2

Ved å estimere både et steg frem og tilbake vil endringen som skjer et steg frem kanselleres noe med endringen som skjer bak punktet vi jobber rundt. Igjen vil den monotont stigende kvaliteten til e^x bety at dette fører til litt høye estimater, frem til avrundingsfeil begynner å tulle til svarene. Uansett er estiimatene dramatisk bedre og når et bunnpunkt med steglengde på 10e-5 i stedet for 10e-8 som i oppgave 1. Atpåtil er feilen nesten på skala med 10e-10 i stedet for 10e-8 slik som oppgave 1.

![alt text](https://github.com/SimonEideHubs/TMA4106-oblig/blob/master/oppg2_1.png?raw=true)

Igjen trekkes pythons beste beregnede analytiske verdi fra estimatene og den absolutte feilen plottes på logaritmisk skala. Feilen faller igjen lineært i det logaritmiske regime, men denne gangen med omtrent dobbel hastighet. Nå bruker vi en andre-ordens estimering, og det vil si at vi forventer at feilen skal falle med omtrent to størrelsesordner for en i steglengden. Det ser riktig ut i forhold til plottet.

![alt text](https://github.com/SimonEideHubs/TMA4106-oblig/blob/master/oppg2_2.png?raw=true)

### Oppgave 3

På dette punktet er det første plottet nesten nytteløst. I absolutte verdier er allerede det første estimatet så godt at det er vanskelig å tyde. Derimot blir feilen ganske dramatisk når vi nærmer oss grensen for hva oms kan beregnes med denne mengden desimaler. Jeg legger ved det første plottet, men går rett til å kommentere på feilen i logaritmisk skala, slik den vises i figuren etter. Vi er nå på fjerde-ordens estimering, og vi ser at en steglengde på 10e-1 gir avvik i størrelsesorden 10e-4. Som forventet faller feilen med fire ordner per ene i steglengden, til vi når 10e-12. Tidligere enn noen gang før, men ikke uventet begynner avrundingsfeilen å dominere tidlig.

![alt text](https://github.com/SimonEideHubs/TMA4106-oblig/blob/master/oppg3_1.png?raw=true)

![alt text](https://github.com/SimonEideHubs/TMA4106-oblig/blob/master/oppg3_2.png?raw=true)

## Oppgave 4-6: Varmelikningen estimert med forskjellige metoder

Den 1-domensjoneller varmelikningen er relativt simpel og uttrykker egentlig bare at skarpe gradienter jevnes ut. Dette avhenger egentlig også litt av materialegenskaper etc, men det er ikke poenget her. Vi setter også randkrav, som her bare er null i begge ender. Dette kunne vært anderledes om en kilde var satt på den ene siden, men dette er igjen ikke poenget her. Deretter settes en startsposisjon som kommer til å gjevne seg ut over tid, frem til all varme er jevnt fordelt. SIden randkravene her er null i begge ender vil det bety at temperaturen går mot null overalt. Om det er ønskelig eller realistisk å finne en analytisk løsning er det mulig å finne gode estimater ved å diskretisere både tid og rom og estimere verdiene for alle punktene for alle tidene. Dette er hovedsaklig gunstig på grunn av moderne datamaskiner som kan kverne millioner av kalkulasjoner i sekundet. Dette tillater også gode - om enn ikke perfekte - modelleringer av kompliserte scenarioer. Dette brukes for eksempel mye i utvikling av fotoniske integrerte kretser, der "Finite-difference Time Domain" (FDTD) bruker for å observere og bekrefte funskjonen til en struktur. 

Varmelikningen estimeres her med tre forskjellige metoder:
- Eksplisitt - Uttrykket for den neste verdien i et punkt er bare basert på tidligere verdier i dette punktet samt naboverdiene. Dette kan beregnes direkte: \
    $u_i^{n+1}=u_i^n+\frac{k}{h^2}(u_{i+1}^n-2u_i^n+u_{i-1}^n)$
  
- implisitt - Uttrykket for den neste verdien i punktet inneholder seg selv og er derfor "Implisitt" definert. Det vil si at den fremtidige verdien er "Gjemt" i noen matrise-operasjoner: \
    $u_i^n = \left(1+2\lambda\right)u_i^{n+1}-\lambda u_{i+1}^{n+1}-\lambda u_{i-1}^{n+1}$ \
    $(I+\lambda A)\mathbf{u}^{n+1}=\mathbf{u}^n$
  
- Crank-Nicolson - Noe analogt med sentraldifferansen bruker denne metoden gjennomsnittet av steg for å balansere ut ugjevnheter fra enkeltsteg. På denne måten blir resultatet ganske likt med den implisitte metoden, men også       litt hermende av sentraldifferansen: \
    $(I+\frac{\lambda}{2}A)u^{n+1}=(I-\frac{\lambda}{2}A)u^n$



### Oppgave 4

