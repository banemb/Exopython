
"""
    #programme qui lit un fichier
"""

if __name__ == "__main__":
    file =open("animaux.txt", "r")
    fileRead = file.readlines()
    for animal in fileRead:
        print(animal)

""" 
    #Autre methode
    with open("animaux.txt","r") as filin:
        ligne = filin.readline()
        while ligne != "":
            print(ligne)
            ligne = filin.readline()
"""

#Ecriture dans un fichier
animauxNew =["pichou" ,"merco" ,"junior","dilan" ,"bojo"]
with  open("animaux.txt", "w") as animauxName:
    for name in animauxNew:
        animauxName.write(f"{name} \n")

