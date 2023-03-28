# Créer une classe “Rectangle” avec comme attribut privé longueur et largeur. Créer la
# méthode “périmètre” permettant de calculer le périmètre du rectangle ainsi que la
# méthode “surface“ permettant de calculer la surface du rectangle.
# Créer les accesseurs et mutateurs permettant de manipuler les attributs de la classe.
# Créer une classe “Parallélépipède“ héritant de la classe Rectangle avec en plus un
# attribut hauteur et une autre méthode volume permettant de calculer le volume du
# parallélépipède.
# Instancier la classe Rectangle et assurez-vous que toutes les méthodes fonctionnent.

class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        perimetre = (self.__largeur + self.__longueur) * 2
        return perimetre
    
    def surface(self):
        surface = (self.__longueur * self.__largeur)
        return surface
    
    def setLongeur(self, longueur):
        self.__longueur = longueur
    
    def setLargeur(self, largeur):
        self.__largeur = largeur

class Parallélépipède(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.hauteur = hauteur

    def volume(self):
        volume = (self.surface() * self.hauteur)
        return volume

rectangle = Rectangle(10,5)
print(rectangle.perimetre())

rectangle.setLargeur(15)
rectangle.setLongeur(7)
rectangle.perimetre()

print(rectangle.perimetre())
parallélépipède = Parallélépipède(10,10,5)
print(parallélépipède.volume())