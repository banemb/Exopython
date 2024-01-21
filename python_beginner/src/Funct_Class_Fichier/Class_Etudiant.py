"""
    #creons une petite classe python reprentez un etudiant
    #la classe aura attributs noms , age et notes
"""
#fonction remplir note
def remplir():
    NotesEtu =[]
    nbreNote = int(input("Combien de notes voulez vous entrez ? : "))
    for i in range(nbreNote):
        note = float(input(f'Entrez la {i+1} eime note: '))
        NotesEtu.append(note)
        len(NotesEtu)
    return NotesEtu


class Etudiant :
    NomEtu :str
    AgeEtu :int
    NotesEtu =[]

    #Constructor
    def __init__(self , nom:str ,age:int ,notes):
        self.NomEtu = nom
        self.AgeEtudiant = age
        self.NotesEtu = notes

    def moyenne (self):
        note = 0
        for i in self.NotesEtu:
            note = note + i
        moyen = note /len(self.NotesEtu)
        print(f"la moyenne est {moyen}")

    def getNoteEtu(self):
        return self.NotesEtu


if __name__ =="__main__":
    #remplir note Etudiant
    NoteEtu =remplir()

    #instanciation d'un etudiant
    etudiant = Etudiant("pichou" ,12,NoteEtu)

    #moyenne etudiant
    print(etudiant.getNoteEtu())

    #Moyenne de l'etudiant
    etudiant.moyenne()
