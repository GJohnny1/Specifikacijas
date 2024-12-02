import random
lielieBurti = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
mazieBurti = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
cipari = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
simboli = ["!","@","#","$","%","^","&","*","(",")","-","_","+","="]
parole = []


garums1 = int(input("Ievadiet vajadzīgo paroles garumu(8-128):"))
stiprums = input("Ievadiet (cipari, simboli, lielie burti, mazie burti)")
    
for i in range(garums1):
    if "cipari" in stiprums:
        parole.append(cipari[random.randint(0, len(cipari) - 1)])
    if "simboli" in stiprums:
        parole.append(simboli[random.randint(0, len(simboli) - 1)])
    if "lielie burti" in stiprums:
        parole.append(lielieBurti[random.randint(0, len(lielieBurti) - 1)])
    if "mazie burti" in stiprums:
        parole.append(mazieBurti[random.randint(0, len(mazieBurti) - 1)])

for i in parole:
    print(parole[random.randint(0, len(parole) - 1)], end="")
    
    
        
