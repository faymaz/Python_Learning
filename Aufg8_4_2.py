liste = [3, 6, 123, 54, 927]
print (liste)
for inhalt in enumerate(liste):
 liste[inhalt[0]] = inhalt[1] * 2
print (liste)
