"""
   #ecrivons un programme python qui prend
   #en entree les notes de trois exemans
   #pour un etudiant et calcule sa moyenne .
   #Ensuite  affiches la moyenne calcculé
"""


if __name__ == "__main__" :
   print("Entrez les notes de trois exemans ")

   #les notes de trois exemans
   noteUne = float(input("note un : "))
   noteDeux = float(input("note deux : "))
   noteTrois = float(input("note trois : "))

   #calcule sa moyenne
   moyenne = (noteUne + noteDeux + noteTrois)/3

   # afficheons la moyenne calcculé
   print(f"La moyenne est :  {moyenne}")