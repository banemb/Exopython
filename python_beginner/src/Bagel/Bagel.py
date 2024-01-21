
#verificationde la taille du nombre
def tailleNombre(nombre:int):
    while(len(str(nombre)) >= 2):
        nombre = int(input("Entrez un autre chiffre: "))
    return nombre

#remplissage du tablesu

def EmptyArray():
    arr = []
    for i in range(0,3):
        value = int(input("Entrez un nombre : "))
        # verificationde la taille du nombre
        value = tailleNombre(value)
        while (value in arr):
            value = int(input("Entrez un autre nombre car il deja dans la tableau : "))
            # verificationde la taille du nombre
            value = tailleNombre(value)
        arr.append(value)
    #return du tableau
    return arr

if __name__ == "__main__":
    arr = EmptyArray()
    print(arr)