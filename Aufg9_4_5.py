"""
import modul_bsp
eingabe = eval(input("Geben Sie eine Zahl ein: "))
print (modul_bsp.formel(eingabe))

import module.modul_bsp
eingabe = eval(input("Geben Sie eine Zahl ein: "))
print (module.modul_bsp.formel(eingabe))
"""

import module.modul_bsp
formel = module.modul_bsp.formel
eingabe = eval(input("Geben Sie eine Zahl ein: "))
print (formel(eingabe))
