# Créer une classe “Operation” avec un constructeur (méthode qui sera appelée lors de
# l’instance de la classe). Ajouter les attributs “nombre1” et “nombre2” initialisés avec des
# valeurs par défaut. Instancier votre première classe et imprimer l’objet en console.

class Operation:
    
    def __init__(self):
        self.nombre1 = 0
        self.nombre2 = 1
    
op = Operation()
print(op)
