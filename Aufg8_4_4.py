liste = [12, 18, 3, 6, 0, 46, 234, 23]
wert = eval(input("Welcher Wert soll dividiert werden? "))
for n in liste:
    if n == 0:
        print ("Fehler: Zahlen dürfen nicht durch 0 geteilt werden")
        continue
    print (wert/n)
