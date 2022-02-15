quiz_erdkunde_1 = ["Hauptstadt von Frankreich ", "Paris"]
quiz_erdkunde_2 = ["Hauptstadt von Deutschland ", "Berlin"]
quiz_erdkunde_3 = ["Hauptstadt von der USA ", "Washington"]
quiz_erdkunde_4 = ["Hauptstadt von China ", "Peking"]
quiz_erdkunde_5 = ["Hauptstadt von Russland ", "Moskau"]

quiz_math_1 = ["25 + 30 = ", 55]
quiz_math_2 = ["8 x 3 = ", 24]
quiz_math_3 = ["12 + 26 = ", 38]
quiz_math_4 = ["3 x 15 = ", 45]
quiz_math_5 = ["48 - 14 = ", 34]

b=0
print(" Hallo Baha!!!, \n Du hast 5 Fragen zu beantworten. Wenn du mindestens 3 richtig beantwortest, bekommst du als Belohnung Handyspielzeit. Wenn du 2 oder 1 richtig beantwortest, dann darfst du nur mit MIR !!! Minecraft spielen.\n\n\t")

a = eval(input(quiz_math_1[0]))
if (quiz_math_1[1] == a):
    print("\nJa du hast es gewusst!!!", a)
    b+=1
else:
    print("\nohh nein du hast es nicht gewusst!!!", a)

a = eval(input(quiz_math_2[0]))

if (quiz_math_2[1] == a):
    print("\nJa du hast es gewusst!!!", a)
    b+=1
else:
    print("\nohh nein du hast es nicht gewusst!!!", a)

a = eval(input(quiz_math_3[0]))

if (quiz_math_3[1] == a):
    print("\nJa du hast es gewusst!!!", a)
    b+=1
else:
    print("\nohh nein du hast es nicht gewusst!!!", a)

a = eval(input(quiz_math_4[0]))
if (quiz_math_4[1] == a):
    print("\nJa du hast es gewusst!!!", a)
    b+=1
else:
    print("\nohh nein du hast es nicht gewusst!!!", a)

a = eval(input(quiz_math_5[0]))
if (quiz_math_5[1] == a):
    print("\nJa du hast es gewusst!!!", a)
    b+=1
else:
    print("\nohh nein du hast es nicht gewusst!!!", a)


a = input(quiz_erdkunde_1[0])
if (quiz_erdkunde_1[1] == a):
    print("\nJa du hast es gewusst!!!", a)
    b+=1
else:
    print("\nohh nein du hast es nicht gewusst!!!", a)


a = input(quiz_erdkunde_2[0])
if (quiz_erdkunde_2[1] == a):
    print("\nJa du hast es gewusst!!!", a)
    b+=1
else:
    print("\nohh nein du hast es nicht gewusst!!!", a)


a = input(quiz_erdkunde_3[0])
if (quiz_erdkunde_3[1] == a):
    print("\nJa du hast es gewusst!!!", a)
    b+=1
else:
    print("\nohh nein du hast es nicht gewusst!!!", a)

a = input(quiz_erdkunde_4[0])
if (quiz_erdkunde_1[1] == a):
    print("\nJa du hast es gewusst!!!", a)
    b+=1
else:
    print("\nohh nein du hast es nicht gewusst!!!", a)

a = input(quiz_erdkunde_5[0])
if (quiz_erdkunde_1[1] == a):
    print("\nJa du hast es gewusst!!!", a)
    b+=1
else:
    print("\nohh nein du hast es nicht gewusst!!!", a)

if (b >= 1) and (b <= 2):
    print("\n",b,", Punkt Viele Fehler: weitere Übung erforderlich!")
elif (b >= 3) and (b <= 4):
    print("\n",b,", Punkte Gute Leistung!")
elif b == 5:
    print("\n",b,", Punkte Super! Alle Aufgaben richtig gelöst!!!")
else:
    print("\n",b,", Punkt Dringend Nachhilfe benötigt!")
