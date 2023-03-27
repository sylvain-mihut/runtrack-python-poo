# Modifier votre classe “Operation” afin d’y ajouter la méthode addition. Cette méthode
# additionne “nombre1” et “nombre2” et affiche en console le résultat.

class Operation:
    
    def __init__(self):
        self.nombre1 = 2
        self.nombre2 = 1
    
    def addition(self):
        # self.add = self.nombre1 + self.nombre2
        return self.nombre1 + self.nombre2


op = Operation()
op.addition()
