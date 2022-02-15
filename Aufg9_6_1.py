def zweierschritte (a, b):
 if a < b:
  for x in range (a, b + 1, 2):
   print (x)
 else:
  for x in range (a, b - 1, -2):
   print (x)

wert1 = eval(input("Geben Sie bitte die erste Zahl ein: "))
wert2 = eval(input("Geben Sie bitte die zweite Zahl ein: "))
zweierschritte(wert1, wert2)
