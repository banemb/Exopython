"""
    Écrivez un programme qui compte le nombre de voyelles dans une chaîne de caractères.
"""

#function de verification d'une voyelle
def voyelle(mot:str):
    # tab de voyelle
    TabVoyelle = ['a', 'e', 'i', 'o', 'u', 'y']
    if mot in TabVoyelle:
        return True
    else:
        return False



if __name__ == "__main__":
    print("hello world")
    #tab de voyelle
    count = 0

    #print chaine de caractere
    word=str(input("Entrez un phrase : "))

    #traitement
    for mot in word:
        if voyelle(mot):
            count = count + 1
            print(mot,count)

    #Affichage du nomnre de voyelle
    print('Le nombre de voyelle dans cette phrase est : ',count)