"""
    Écrivez un programme qui trouve tous les nombres premiers jusqu'à un certain nombre donné.
"""
#nombre premier
def est_premier(nombre:int):
    if nombre == 1:
        return True
    for j in range (2 ,int(nombre**0.5)+1):
        if nombre % j == 0:
            return False
    else:
        return  True


if __name__ == "__main__":
    print("un programme qui trouve tous les nombres premiers jusqu'à un certain nombre donné")

    #nombre d'iteration
    nombreIteration=int(input('Entrez le un nombre donné : '))

    #tableau de nombre premier
    tabPremier = []

    #instruction for
    for i in range (1,nombreIteration):
        if est_premier(i):
            tabPremier.append(i)
    print(tabPremier)