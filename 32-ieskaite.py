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
