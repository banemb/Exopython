"""
     Écrivez un programme qui vérifie si un nombre est pair ou impair.
"""

if __name__ == "__main__":
    number = int(input("Entrez un bombre : "))
    if number % 2 == 0:
        print(number ," est pair")
    else:
        print(number , ' est impair')