class Polinomio():

        def __init__(self, value):
            self.polinomio = value
    

    def suma(otroPolinomio):
        if len(self.polinomio > otroPolinomio):
            solucion = self.polinomio

            for x in range(len(otroPolinomio)):
                solucion[x] += otroPolinomio[x]
        else:
            solucion = otroPolinomio

            for x in range(len(self.polinomio)):
                solucion[x] += self. polinomio[x]   
        
        return solucion

    def resta(otroPolinomio):
        if len(self.polinomio > otroPolinomio):
            solucion = self.polinomio

            for x in range(len(otroPolinomio)):
                solucion[x] -= otroPolinomio[x]
        else:
            solucion = otroPolinomio

            for x in range(len(self.polinomio)):
                solucion[x] -= self. polinomio[x]   
        
        return solucion

    def producto(otroPolinomio):
        solucion = [0] * (len(self.polinomio) + len(otroPolinomio))
