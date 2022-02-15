#for n in range(100):
# print (n+1)

#for n in range(1,101)
# print(n)

#for n in range(1,101,2)
# print(n) 2 schrittweise

#liste = [12, 18, 3, 6, 46, 234, 23]
#wert = eval(input("Welcher Wert soll gesucht werden? "))
#b=0   b ist fur die stelle
#for n in liste:
#if n == wert:
#  print ("Die Zahl wurde gefunden.")
#  break
# print (b1, n)

liste = [12, 18, 3, 6, 46, 234, 23]
wert = eval(input("Welcher Wert soll gesucht werden? "))
for n in liste:
 if n == wert:
  print ("Die Zahl wurde gefunden.")
  break
 print (n)
else:
 print("Die Zahl ist nicht in der Liste enthalten")
