import module.modul_user
benuzer = module.modul_bsp.benuzer
user = eval(input("Geben Sie benutzername ein: "))
password = eval(input("Geben Sie passwort ein: "))
print (benuzer(user, password))
