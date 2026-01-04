from algemene_functies import mijn_functie_2

#opdracht5
def aanbieding_1(smaak, prijs, korting):
   prijs_na_korting = prijs * (1 - korting) 
   uitvoer =  f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak van {smaak}, van {prijs} euro, voor {prijs_na_korting:.2f} euro."
   return uitvoer
print(aanbieding_1("aardbei",4,0.1))


#opdracht6-7
def inkomsten_totaal(inkomsten, btw):
   totaal = sum(inkomsten)
   bedrag = totaal * float(btw)
   uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."
   return uitvoer
print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09))

#opdracht8
def laag_en_hoog(mijn_lijst):
   hoog = max(mijn_lijst)
   laag = min(mijn_lijst)
   return hoog , laag
print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))

#opdracht9
def gemiddelde(mijn_lijst):
   bedrag = sum(mijn_lijst) / len(mijn_lijst)
   uitvoer = f"De gemiddelde inkomsten deze week zijn {int(bedrag)} euro."
   return uitvoer
print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))

#opdracht 10
def meervoudig (invoer_lijst):
   return laag_en_hoog(invoer_lijst)
print(meervoudig([10,5,3,2,1,2,9]))
   

#opdracht12
def combinatie(invoer_lijst_2):
   korte_lijst = laag_en_hoog(invoer_lijst_2)
   uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
   return uitvoer


