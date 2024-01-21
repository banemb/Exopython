import random as rd

if __name__== "__main__":

    #petite description de notre jeu ,ce programme s'appele jeu_de_devinettes
    #l'utilisateur va entrer un interval de notre entier et
    #deviner le nombre aleatoire generer grace a cette interval


    #name user
    name = str(input("entrer votre nom :  "))
    #presentation
    print('bienvenu sur jeu_de_devinettes entrer un interval souhaitez')
    a = int(input("entrer l'interval inferieur "))
    b = int(input("entrer l'interval superrieur "))

    while a > b:
        a = int(input("entrer l'interval inferieur  (il doit etre inferieur a l'interval superrieur  ) "))
        b = int(input("entrer l'interval superrieur "))

    nmbre_devinette = rd.randint(a,b)
    nmbre_utilisateur = int(input('Bien , essayer de devinet un nombre dans cet interval \n '))

    #Condition de reussite
    nmbre_de_fois = 0
    while nmbre_devinette != nmbre_utilisateur:
        if nmbre_devinette > nmbre_utilisateur :
            nmbre_utilisateur = int(input('entrz un nombre plus grand  '))
        else:
            nmbre_utilisateur = int(input('entrez un nombre plus petit  '))
        nmbre_de_fois += 1

    print(f'Bravo {name}!!! ,vous avez deviner le bon nombre apres {nmbre_de_fois} essaies')

    #condition pour continuer

    continuer = str(input('voulez vous continuer yes/no : '))
    while continuer == 'yes' :
        a = int(input("entrer l'interval inferieur "))
        b = int(input("entrer l'interval superrieur "))

        while a > b:
            a = int(input("entrer l'interval inferieur  (il doit etre inferieur a l'interval superrieur  ) "))
            b = int(input("entrer l'interval superrieur "))

        nmbre_devinette = rd.randint(a, b)
        nmbre_utilisateur = int(input('Bien , essayer de devinet un nombre dans cet interval \n  '))

        # Condition de reussite
        nmbre_de_fois = 0
        while nmbre_devinette != nmbre_utilisateur:
            if nmbre_devinette > nmbre_utilisateur:
                nmbre_utilisateur = int(input('entrz un nombre plus grand : '))
            else:
                nmbre_utilisateur = int(input('entrez un nombre plus petit : '))
            nmbre_de_fois += 1

        print(f'Bravo {name}!!! ,vous avez deviner le bon nombre apres {nmbre_de_fois} essaies')

        continuer = str(input('voulez vous continuer yes/no : '))
    if continuer == "no":
        print(f"Aurevoir  {name} a la prochaine ")