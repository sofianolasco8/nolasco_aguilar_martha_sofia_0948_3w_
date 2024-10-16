print(" ")
print("nolasco_aguilar_martha_sofia_0948_2W")
print(" ")
thisdict = {
    "euro": "€",
    "dollar":"$",
    "yen":"¥",
}
divisa = input("ingresa una variable ")
if divisa in thisdict:
    print("la divisa esta dentro del diccionario ")
elif divisa != thisdict:
    print("la divisa no esta dentro del diccionario")