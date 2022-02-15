markeFahrzeug1 = "VW"
modellFahrzeug1 = "Golf"
baujahrFahrzeug1 = 2011
preisFahrzeug1 = 5000

markeFahrzeug2 = "Renault"
modellFahrzeug2 = "Clio"
baujahrFahrzeug2 = 2013
preisFahrzeug2 = 6000

markeFahrzeug3 = "Porsche"
modellFahrzeug3 = "Panamera"
baujahrFahrzeug3 = 2014
preisFahrzeug3 = 25000

markeFahrzeug4= "BMW"
modellFahrzeug4= "Grantourer"
baujahrFahrzeug4 = 2016
preisFahrzeug4= 8000

fahrzeug_1 = ["VW", "Golf", 2011, 5000]
fahrzeug_2 = ["Renault", "Clio", 2013, 6000]
fahrzeug_3 = ["Porsche", "Panamera", 2014, 25000]
fahrzeug_4 = ["BMW", "Grantourer", 2016, 8000]



fahrzeug1 = {"marke": "VW", "modell": "Golf", "baujahr": 2011, "preis": 5000}
fahrzeug2 = {"marke": "Renault", "modell": "Clio", "baujahr": 2013, "preis": 6000}
fahrzeug3 = {"marke": "Porsche", "modell": "Panamera", "baujahr": 2014, "preis": 25000}
fahrzeug4 = {"marke": "BMW", "modell": "Grantourer", "baujahr": 2016, "preis": 8000}


fahrzeug1 = dict ([("marke", "VW"), ("modell", "Golf"), ("baujahr", 2012), ("preis", 5000)])
fahrzeug1 = dict (marke="VW", modell="Golf", baujahr=2012, preis=5000)

Hierbei wird der entsprechende Begriff stets als Zeichenkette gespeichert. Wenn man in diesem Fall eine Zahl als Schlüssel eingibt, führt das jedoch zu einem Fehler.
