# TMA4106-oblig
Standardprosjekt for oblig i TMA4106 fordi jeg er travel.

All kode som hører til en oppgave ligger i python-fila med tilsvarende navn.

## Oppgave 1

Denne metoden bruker bare et steg frem til å estimere den nåværende verdien. Derfor vil den nesten utelukkende (Foruten nærværet av andre feil) estimere for høyt for en funskjon som e^x. Dette er fordi den førstederiverte av e^x stiger monotont (Og såklart er e^x i seg selv).
Observerer slik det er forventet at presisjonen starter ganske dårlig til å begynne med, men blir bedre i proporsjon med steglengden. dette fortsetter frem til steglengden 10e-8 der estimated er nærmest den analytiske verdien ned til de 16 desimalene python jobber med her. Deretter stiger feilen igjen, siden avrundingsfeilen bare blir større og større. Dette synes litt i det føeste bildet, som viser estimat sammenliknet med forventer verdi, men best i andre figur som viser feil på logaritmisk skala.
![alt text](https://github.com/SimonEideHubs/TMA4106-oblig/blob/master/oppg1_1.png?raw=true)
Siden feilen fort blir veldig liten relativt til verdiene, blir denne grafen fort lite hjelpsom. Neste viser heller avvik fra forventet verdi (Med 16 desimalers presisjon) på logaritmisk skala. Her ser vi at feilen faller omtrent med en størrelsesorden for hver størrelsesorden i steglengden.
![alt text](https://github.com/SimonEideHubs/TMA4106-oblig/blob/master/oppg1_2.png?raw=true)


## Oppgave 2

Ved å estimere både et steg frem og tilbake vil endringen som skjer et steg frem kanselleres noe med endringen som skjer bak punktet vi jobber rundt. Igjen vil den monotont stigende kvaliteten til e^x bety at dette fører til litt høye estimater, frem til avrundingsfeil begynner å tulle til svarene. Uansett er estiimatene dramatisk bedre og når et bunnpunkt med steglengde på 10e-5 i stedet for 10e-8 som i oppgave 1. Atpåtil er feilen nesten på skala med 10e-10 i stedet for 10e-8 slik som oppgave 1.

![alt text](https://github.com/SimonEideHubs/TMA4106-oblig/blob/master/oppg2_1.png?raw=true)

Igjen trekkes pythons beste beregnede analytiske verdi fra estimatene og den absolutte feilen plottes på logaritmisk skala. Feilen faller igjen lineært i det logaritmiske regime, men denne gangen med omtrent dobbel hastighet. Det vil si at feilen ser ut til å falle med omtrent to størrelsesordner for en i steglengden.

![alt text](https://github.com/SimonEideHubs/TMA4106-oblig/blob/master/oppg2_2.png?raw=true)

## Oppgave 3

På dette punktet er det første plottet nesten nytteløst. I absolutte verdier er allerede det første estimatet så godt at det er vanskelig å tyde. Derimot blir feilen ganske dramatisk når vi nærmer oss grensen for hva oms kan beregnes med denne mengden desimaler. Jeg legger ved det første plottet, men går rett til å kommentere på feilen i logaritmisk skala, slik den vises i figuren etter.

