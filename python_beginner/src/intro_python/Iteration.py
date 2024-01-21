"""
    #ecrivons un programme qui demande a l'utilisateur de saisir
    #un entier positif ,puis affiche tous les nombres pairs
    #de 0 jusqu'a l'entier saisi
"""


if __name__ == "__main__":

    #on demande a l'utilisateur de saisir
    nbre = int(input('entrez un nombre : '))

    #boucle qui calcule puis affiche tous les nombres pairs
                #de 0 jusqu'a l'entier saisi
    for i in range(nbre+1):
        nbrePair = i%2
        if (nbrePair==0 ):
            print(f"{i}")