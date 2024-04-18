'''
Automobilių parkas. Susideda iš:

Lengvųjų automobilių;

Keleivių pervežimo automobiliai;

Krovinių pervežimo automobiliai.



Autobusai turimi atributai:

Keleivių vietų skaičius

Skaičiuojamas kilometražas per metus (tam, kad suskaičiuoti kokie yra kintami kaštai vienam kilometrai)

Automobilio numeris;

Kuro tipas;

Pastovūs kaštai (draudimas, techninės apžiūros ir t.t.) Eurai per metus;

Techninės apžiūros datos;

Vairuotojo (priklauso nuo teisių kategorijų) teisių kategorijos;

Kuro sąnaudos 100km.

Draudimo data

Reikalingi metodai:

Metodas, kuris paskaičiuotų ar sekantį mėnesį reikia atlikti technine apžiūra, ar reikia draudimo;

Paskaičiuoti kokie bus kaštai nuvažiavus atstumą X. Reikia įvertinti pastovius kaštus, kuro kainą;

Metodas, kiek reikia autobusų norint pervežti N keleivių;

Paskaičiuotų kokia būtų bendra samata pervežus N keleivių ir nuvažiavus X kilometrų.



Lengvųjų turimi atributai:

Skaičiuojamas kilometražas per metus (tam, kad suskaičiuoti kokie yra kintami kaštai vienam kilometrai)

Automobilio numeris;

Kuro tipas;

Pastovūs kaštai (draudimas, techninės apžiūros ir t.t.) Eurai per metus;

Techninės apžiūros datos;

Vairuotojo (priklauso nuo teisių kategorijų) teisių kategorijos;

Kuro sąnaudos 100km.

Draudimo data

Reikalingi metodai:

Metodas, kuris paskaičiuotų ar sekantį mėnesį reikia atlikti technine apžiūra, ar reikia draudimo;

Paskaičiuoti kokie bus kaštai nuvažiavus atstumą X. Reikia įvertinti pastovius kaštus, kuro kainą;





Krovininiai automobiliai:

Skaičiuojamas kilometražas per metus (tam, kad suskaičiuoti kokie yra kintami kaštai vienam kilometrai)

Pervežimas svoris

Yra galimybė prikabinti priekabą ar ne;

Priekabos pervežiamas svoris

Automobilio numeris;

Kuro tipas;

Pastovūs kaštai (draudimas, techninės apžiūros ir t.t.) Eurai per metus;

Techninės apžiūros datos;

Vairuotojo (priklauso nuo teisių kategorijų) teisių kategorijos;

Kuro sąnaudos 100km.

Draudimo data

Reikalingi metodai:

Metodas, kuris paskaičiuotų ar sekantį mėnesį reikia atlikti technine apžiūra, ar reikia draudimo;

Paskaičiuoti kokie bus kaštai nuvažiavus atstumą X. Reikia įvertinti pastovius kaštus, kuro kainą;

Paskaičiuoti kiek reisų reikia padaryti ir ar reikia prikabinti priekabą (tarkim reikia pervežti 30, automobilio pervežamas svoris yra 12 tonų, priekabos pervežamas svoris 5 tonos. Tokiu atveju reikia vieną karta vežti be priekabos, o antra su priekaba. Bet jei reikia pervežti tarkime 36 tonos, priekabos kabinti neverta, nes vistiek reikia daryti tris reisus);





Vairuotojas, kuris turi atributus:

Atostogų laikas

Turima teisių kategorija (D sukvežimiai be priekabos, E su priekaba)

Darbo užmokestis vienam kilometrui;



Prie sukvežimių:

pridėkime metodą, kuris vertintų vairuotoją ir pagal turimą kategoriją įvertintų ar gali vairuoti mašina su priekaba.

Visiems automobiliams turi būti patikrinimas ar vairuotojas gali dirbti (ne atostogauja)
'''