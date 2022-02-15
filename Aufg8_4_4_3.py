"""
weiter = "true"
while weiter == "true":
 zahl = eval(input("Welche Zahl möchten Sie verdoppeln? "))
 print("Doppelter Wert: ", zahl * 2)
 weiter = input ("Möchten Sie fortfahren? (true/false)")
"""




while True:
 zahl = eval(input("Welche Zahl möchten Sie verdoppeln? "))
 print("Doppelter Wert: ", zahl * 2)
 weiter = input ("Möchten Sie fortfahren? (ja/nein) ")
 if weiter != "ja":
  break
