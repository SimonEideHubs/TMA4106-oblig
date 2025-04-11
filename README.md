# TMA4106-oblig
Standardprosjekt for oblig i TMA4106 fordi jeg er travel.

## Oppgave 1

All kode som hører til oppgaven er i fila med tilhørende navn.
Observerer slik det er forventet at presisjonen starter ganske dårlig til å begynne med, men blir bedre i proporsjon med steglengden. dette fortsetter frem til steglengden 10e-8 der estimated er nærmest den analytiske verdien ned til de 16 desimalene python jobber med her. Deretter stiger feilen igjen, siden avrundingsfeilen bare blir større og større. Dette synes litt i det føeste bildet, som viser estimat sammenliknet med forventer verdi, men best i andre figur som viser feil på logaritmisk skala.
![alt text](https://github.com/SimonEideHubs/TMA4106-oblig/blob/master/oppg1_1.png?raw=true)
Siden feilen fort blir veldig liten relativt til verdiene, blir denne grafen fort lite hjelpsom. Neste viser heller avvik fra forventet verdi (Med 16 desimalers presisjon) på logaritmisk skala. Her ser vi at feilen faller omtrent med en størrelsesorden for hver størrelsesorden i steglengden
![alt text](https://github.com/SimonEideHubs/TMA4106-oblig/blob/master/oppg1_2.png?raw=true)
