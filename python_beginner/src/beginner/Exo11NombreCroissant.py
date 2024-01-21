"""
    Écrivez un programme qui trie une liste d'entiers dans l'ordre croissant
"""
#fonction qui nous permet de classer notre tableau
def tab_Classe(tab):
    b=0
    for j in range(0,len(tab)-1):
        a = j+1
        if (tab[j]>tab[a]):
            b = tab[a]
            tab[a]=tab[j]
            tab[j]=b

    return tab
if __name__ == "__main__":
    print("Hello , World")
    Tab=[]
    #Taille du tableau
    taille = int (input('Voulez vous trier combien de nombre : '))

    #Remplisage du tableau
    for i in range (0 ,taille):
        nombre = float(input(f'Entrez le {i+1} ieme nombre : '))
        Tab.append(nombre)

    #affichage du tableau non trie
    tabTrie = tab_Classe(Tab)
    print(Tab)
    print(tabTrie)