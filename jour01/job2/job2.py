# À l’aide de la classe “Operation” crée au-dessus, imprimer en console la valeur des
# attributs “nombre1” et “nombre2”.


class Operation:

    def __init__(self):
        self.nombre1 = 0
        self.nombre2 = 1
    
op = Operation()
print(op.nombre1, op.nombre2)
