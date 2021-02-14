def foto(filma, kadruSkaits, skaits, izmers):
    cenaVienam = 0
    kadruSkaits = 0

    if C-41 == "KRĀSU NEGATĪVAJĀM":
        cenaVienam = 1
    elif MB == "MELNBALTAJĀM FILMĀM":
        cenaVienam = 2,25
    elif NONE == "NAV JĀATTIĪSTA":
        cenaVienam = 0

    pasutijumaCena = cenaVienam * skaits

    if pasutijumaCena > 99:
        pasutijumaCena = pasutijumaCena * 0,22

    if piegade and pasutijumaCena < 100:
        kadruSkaits = 0,18

    jamaksa = pasutijumaCena + kadruSkaits
    return jamaksa



##1) Kas vislabak izdodas, veicot specifikāciju uzdevumus?
##Es uzkatu, ka vislabāk bija rakstīti tos if un elif
##2) Ko vel jāuzlabo, lai specifikāciju uzdevumu risināšana izdotos labāk?
##Ir diezgan pagrūti vēl bet es lēnām sāku saprast, šo darbu es mēģināju skatīties
##pēc iepriekšējās stundas paraugu
##3) Ar kādu atzīmi novērtē savu šodienas darbu?
##6
print(foto('MB', 36, 1, '9x13'))
print(foto('C-41', 24, 4, '10x15'))
print(foto('NONE', 12, 2, '13x18'))

"""
Paldies par darbu!
Jā, t-kreklu uzdevuma ietekmu te var redzēt, bet diemžēl tik līdzīgi tie uzdevumi nebija.

Kas ir Python decimālais atdalītājs . vai ,?

Pirmais sazarojums:
Filmu tipi funkcijā nonāk ar mainīgo filma, tātad tur kods varētu sākties šādi:
if filma=='C-41':
    cenaVienam = 1 # (mainīgā nosakums cenaVienam te gan galīgi neatbilst būtībai)
utt.

Mainīgo piegade uzdevuma prasībās neesmu manījis, tas arī noteikti pārnācis no krekliem.
Manīgais pasutijumaCena Tev izveidojas no filmas tipa reizināta ar skaitu. Nosaukums atkal īsti neatbilst, bet formula pareizi, tas aprēķina filmas attīstīšanas izmaksas.
Bet tām nav nekāda saistība ar skaitļiem 99 un 100, kuri parādas nākamajā programmas blokā. Tajā ir svarīgi pārbaudīt saņemto parametru izmers (līdzīgi kā parametru filma sākumā)
un tad mēģināt sarēķināt, cik izmaksās prasītā fotogrāfiju skaita izgatavošana. To saliekot kopā ar attīstīšanas izmaksām, varētu sanākt vajadzīgā atbilde.
"""
