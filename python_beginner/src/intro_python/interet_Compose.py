"""
    #Écrivez un programme qui calcule le montant final
    #après avoir placé un montant initial à un taux
    #d'intérêt fixe pendant un certain nombre d'années.
"""

if __name__ == "__main__":
    MontantInitial = float(input('entrez le montant initial :'))

    #Taux d'interet fixe 3% par mois
    TauxInteret = 3/100

    #Nombre d'annees
    NombreAnnee = float(input("entrez le nombre d'annees :"))

    #calcule du montant initiale
    MontantFinale = ((MontantInitial *3)/100)*(NombreAnnee*12) + MontantInitial

    #Montant interet compose
    print(f"montant interet est {((MontantInitial *3)/100)}")

    #Montant finale
    print(f"Montant final apres {NombreAnnee} ans est {MontantFinale} FCFA")