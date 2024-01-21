"""
    Écrivez un programme python qui prend en entrée une chaîne de caractères et
    vérifie si elle est un palindrome ou non.
    Un palindrome est une chaîne qui se lit de la même manière de gauche à droite et de droite à gauche.
"""
#fonction qui verifie si c'est un polindrone

if __name__ =="__main__":
    print("vérifie si un mot  est un palindrome ou non.")
    MotPolindrone = (str(input("entrez un mot : "))).lower()

    TrueMotPolindrone = ''
    #renformation en tableau
    for  lettre in range(-1,-(len(MotPolindrone)+1),-1):
        TrueMotPolindrone =TrueMotPolindrone + MotPolindrone[lettre]
    TrueMotPolindrone.lower()
    print(TrueMotPolindrone)

    #verification du mot polindrone
    if TrueMotPolindrone == MotPolindrone :
        print(MotPolindrone ,'est un mot polindrone')
    else:
        print(MotPolindrone," n'est pas un mot polindrone ")
