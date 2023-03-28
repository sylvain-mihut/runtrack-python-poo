# Créer une classe “Rectangle” avec des attributs privés, “longueur” et “largeur” initialisé
# dans le constructeur.
# Créer des assesseurs et mutateurs afin de pouvoir afficher et modifier les attributs de la classe.
# Créer un rectangle avec les valeurs suivantes : longueur 10 et largeur 5. 
# Changer la valeur de la longueur et de la largeur et vérifier que les modifications soient bien prises en compte.


class Rectangle:

    def __init__(self):
        self.__longueur = ""
        self.__largeur = ""

    def setDim(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur 

    def getDim(self):
        return self.__longueur, self.__largeur

rectangle = Rectangle() 

rectangle.setDim(10,5)

print(rectangle.getDim())
