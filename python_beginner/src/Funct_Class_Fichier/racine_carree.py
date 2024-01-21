"""
    #function racine carree
    #puis testons cette fonction
"""
import math

#function racine carree
def racineCarre(a):
    racineCarre = math.sqrt(a)
    return print(f"la racine carrée de {a} est {racineCarre}")




if __name__ == "__main__":
    condition = int(input("combien de racine voulez vous calcules ? :"))
    for i in range(condition):
        nombreRacine=float(input("Veillez entrer le nombre a connaitre sa racine carré :"))
        #test
        racineCarre(nombreRacine)