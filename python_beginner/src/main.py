#debutant poo python avec jonathon
#creation de ma premiere classe personne en python
class Personne:

        #constructeur personne
        def __init__(self,nom : str ="",age: int=0):
            self.nom = nom
            self.age = age
            #affichage du message
            print("je suis le constructeur personne")

#Function demander le nom
        def DemanderNom(self):
            self.nom = input("veuillez entrer votre nom : ")
            return self.nom;

        def SePresenter(self):

            #condition sur l'age
            if self.age ==  0:
                if self.nom == "":
                    nom = self.DemanderNom()
                print(f"mon nom c'est :{self.nom} \n")

            else:
                print(f"mon nom c'est :{self.nom} \n"
                      f"mon age c'est :{self.age} ")
                if self.EstMajeur():
                    print('vous etes majeur')
                else:
                    print("vous etes mineur")
            #function pour connaitre qu'une personne est majeur

        def EstMajeur(self):
            if self.age >= 18:
                return  True;
            else:
                return False;

            #les getter et setter en python
            1#les getters
        def RetounerNom(self):
            return self.nom

        def RetounerPrenom(self):
            return self.prenom

        def RetounerAge(self):
            return self.age

        1  # les setters

        def ModifierNom(self , nom):
            self.nom = nom

        def ModifierPrenom(self , prenom):
             self.prenom =prenom

        def ModifierAge(self, age):
             self.age = age

#programme principale
if __name__ == "__main__":
    # instanciation des personnes
    p1 = Personne("pichou", 20)
    p1.SePresenter()

    #instanciation d'une personne sans argument
    p2= Personne("",0)
    p2.SePresenter()
#On verifie que la personne est majeur ou non
    #print(f"estmajeur :  {p1.EstMajeur()}")