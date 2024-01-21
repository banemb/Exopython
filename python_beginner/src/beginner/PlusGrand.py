"""
    Écrivez un programme qui trouve le plus grand
    nombre parmi trois nombres saisis par l'utilisateur.
"""

if __name__ == "__main__":
    tab=[]
    #inserons les elements dans un tableau
    for i in range(0,3):
        nbre=float(input(f"entrez le {i+1} ieme nombre : "))
        tab.append(nbre)

tab = sorted(tab)
print("le plus grand est :",tab[-1])

