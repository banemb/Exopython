"""
    Écrivez un programme Python qui prend en entrée une liste d'entiers et
    retourne la liste des nombres premiers dans cette liste.
    Un nombre premier est un nombre entier supérieur à 1 qui n'est divisible que par 1 et par lui-même.
"""

    #   fonction qui prend en entrée une liste d'entiers et
    #   retourne la liste des nombres premiers dans cette liste.
def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nombres_premiers(liste):
    premiers = []
    for nombre in liste:
        if est_premier(nombre):
            premiers.append(nombre)
    return premiers


if __name__ == "__main__":
# Exemple d'utilisation
    entrees = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
    resultat = nombres_premiers(entrees)
    print(resultat)