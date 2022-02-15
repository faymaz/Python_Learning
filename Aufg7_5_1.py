#Gebrauchtwagenhaendler
#fahrzeug1 = ["VW",      "Golf", 2012, 8000]
#fahrzeug2 = ["BMW",     "A5",   2011, 5500]
#fahrzeug3 = ["Seat",    "Leon", 2016, 1500]
#
#a = eval(input("Geben Sie bitte den Waren preise ein: "))
#if a >= 6000:
#    print("Preise für dies Waren", fahrzeug1[0:3])
#elif a<=5000:
#    print("Preise für dies Waren", fahrzeug2[0:3])
#elif a<=5000:
#    print("Preise für dies Waren", fahrzeug3[0:3])
#
#
#

fahrzeug1 = ["VW", "Golf", 2011, 5000]
fahrzeug2 = ["Renault", "Clio", 2013, 6000]
fahrzeug3 = ["Porsche", "Panamera", 2014, 25000]
listeFahrzeuge = [fahrzeug1, fahrzeug2, fahrzeug3]
maxpreis = eval(input("Geben Sie bitte den Maximalpreis ein: "))
if listeFahrzeuge[0][3] <= maxpreis:
    print ("Marke: ",listeFahrzeuge[0][0])
    print ("Modell: ",listeFahrzeuge[0][1])
    print ("Baujahr: ",listeFahrzeuge[0][2])
    print ("Preis: ",listeFahrzeuge[0][3], "\n")
if listeFahrzeuge[1][3] <= maxpreis:
    print ("Marke: ",listeFahrzeuge[1][0])
    print ("Modell: ",listeFahrzeuge[1][1])
    print ("Baujahr: ",listeFahrzeuge[1][2])
    print ("Preis: ",listeFahrzeuge[1][3], "\n")
if listeFahrzeuge[2][3] <= maxpreis:
    print ("Marke: ",listeFahrzeuge[2][0])
    print ("Modell: ",listeFahrzeuge[2][1])
    print ("Baujahr: ",listeFahrzeuge[2][2])
    print ("Preis: ",listeFahrzeuge[2][3], "\n")
