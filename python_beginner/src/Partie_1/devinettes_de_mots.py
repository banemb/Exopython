import random as rd

if __name__ == "__main__":
    name = str(input("entrer votre nom:  "))
    print(f"Bonne chance {name} !!")

    #liste des noms
    noms =[ 'pichou' ,'francis' ,'dimitri' ,'junior' ,'bibiche' ,'dilan' ,'hilary' , 'merco' ,'horlane' , 'esther']

    #devinette du mons
    char =str(input('entrer un mot: '))

    words = rd.choice(noms)

    nmbre_de_fois = 0
    while char != words:
        char = str(input('entrez un autre nom  '))
        nmbre_de_fois += 1

    print(f'Bravo {name}!!! ,vous avez deviner le bon nombre apres {nmbre_de_fois} essaies')

    # condition pour continuer

    continuer = str(input('voulez vous continuer yes/no : '))
    while continuer == 'yes':
        noms = ['pichou', 'francis', 'dimitri', 'junior', 'bibiche', 'dilan', 'hilary', 'merco', 'horlane', 'esther']

        # devinette du mons
        char = str(input('entrer un nom: '))

        words = rd.choice(noms)
        nmbre_de_fois = 0
        while char != words:
            char = str(input('entrez un autre nom  '))
            nmbre_de_fois += 1

        print(f'Bravo {name}!!! ,vous avez deviner le bon nombre apres {nmbre_de_fois} essaies')

        continuer = str(input('voulez vous continuer yes/no : '))

        
    if continuer == "no":
        print(f"Aurevoir  {name} a la prochaine ")