"""
import module.modul_user
benuzer = module.modul_bsp.benuzer
user = eval(input("Geben Sie benutzername ein: "))
password = eval(input("Geben Sie passwort ein: "))
print (benuzer(user, password))
"""
def registrierung (nutzername, passwort):
    logindaten = [("karl01", "abcde"), ("*susi*", "qedX01"),("00xyz00", "a7r9f3"), ("martin.mueller", "martin")]
    for zugang in logindaten:
        if zugang[0]==nutzername and zugang[1]==passwort:
            print ("Login erfolgreich!")
            return True
        print ("Nutzernamen und Passwort stimmen nicht überein!")
        return False

wert1 = input("Geben Sie bitte Ihren Nutzernamen ein: ")
wert2 = input("Geben Sie bitte Ihr Passwort ein: ")
angemeldet = registrierung(wert1, wert2)
