"""
    Écrivez un programme qui calcule la factorielle d'un nombre donné.
"""

if __name__ == "__main__":
    nbre =int(input("Entrez un nombre : "))
    fact = 1
    if nbre == 1:
        print(f"le factoriel de {nbre} est {fact}")
    else:
        for i in range (1,nbre+1):
            fact = fact*i
        print(f"le factoriel de {nbre} est {fact}")
