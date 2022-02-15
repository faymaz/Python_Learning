"""
a = eval(input("Geben Sie bitte die Zahl 5 ein: "))
if a == 5:
 print("Die Eingabe ist richtig.")
else :
 print("Sie haben false eingegeben")
a = input('Geben Sie bitte das Wort "HalLo" ein: ')
if a == "Hallo":
    print("Die Eingabe ist richtig.")
a = eval("input(Geben Sie bitte das Wort HalLo ein: )")
if a == "HalLo":
    print("Die Eingabe ist richtig.")
a = eval(input("Geben Sie bitte die Zahl 5 ein: "))
if a == 5:
    print("Die Eingabe ist richtig. ", a)
if a > 5:
    print("Falsche Eingabe! ", a, "Kleiner!!")
if a < 5:
    print("Falsche Eingabe!", a,"Hocher!!")
a = eval(input("Geben Sie bitte die Zahl 5 ein: "))
if a == 5:
    print("Die Eingabe ist richtig.")
if a != 5:
    print("Falsche Eingabe!")

a = eval(input("Geben Sie bitte die Zahl 5 ein: "))
b = eval(input("Geben Sie bitte die Zahl 10 ein: "))
if a == 5 and b == 10:
    print("Die Eingabe ist richtig.")
if not (a == 5 and b == 10):
    print("Falsche Eingabe!")

a = eval(input("Geben Sie bitte die Zahl 5 ein: "))
b = eval(input("Geben Sie bitte die Zahl 10 ein: "))
if a == 5 or b == 10:
    print("Mindestens eine Zahl wurde richtig eingegeben.")
if not (a == 5 or b == 10):
    print("Falsche Eingabe!")
a = eval(input("Geben Sie bitte den Warenbestand ein: "))
if a >= 10 and a < 100:
    print("Die Warenbestände liegen bei", a,"Artikeln.")
elif a >= 100:
    print("Warnung: Keine Lagerkapazitäten mehr frei!")
elif a > 0:  # elif a < 10 and a > 0
    print("Nur noch ", a, "Artikel vorrätig. Bitte nachbestellen!")
elif a == 0:
    print("Warnung: Artikel nicht mehr verfügbar!")
else:
    print("Ungültige Eingabe!")
"""
a = eval(input("Geben Sie bitte den Warenbestand ein: "))
if a >= 100:
    print("Warnung: Keine Lagerkapazitäten mehr frei!")
elif a >= 10:
    print("Die Warenbestände liegen bei", a,"Artikeln.")
elif a > 0:
    print("Nur noch ", a, "Artikel vorrätig. Bitte nachbestellen!")
elif a == 0:
    print("Warnung: Artikel nicht mehr verfügbar!")
else:
    print("Ungültige Eingabe!")
