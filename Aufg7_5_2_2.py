punkte = 0
ergebnis = eval(input("Aufgabe 1: Was ist das Ergebnis aus 6 + 7? "))
if ergebnis == 13:
 punkte = punkte + 1
ergebnis = eval(input("Aufgabe 2: Was ist das Ergebnis aus 12 - 4? "))
if ergebnis == 8:
 punkte = punkte + 1
ergebnis = eval(input("Aufgabe 3: Was ist das Ergebnis aus 4 * 5? "))
if ergebnis == 20:
 punkte = punkte + 1
ergebnis = eval(input("Aufgabe 4: Was ist das Ergebnis aus 24 / 6? "))
if ergebnis == 4:
 punkte = punkte + 1
ergebnis = eval(input("Aufgabe 5: Was ist das Ergebnis aus 5 + 9 + 24? "))
if ergebnis == 38:
 punkte = punkte + 1

if punkte == 0:
 print ("Dringend Nachhilfe benötigt!")
elif punkte < 3:
 print ("Viele Fehler: weitere Übung erforderlich!")
elif punkte < 5:
 print ("Gute Leistung!")
else:
 print ("Super! Alle Aufgaben richtig gelöst!")
