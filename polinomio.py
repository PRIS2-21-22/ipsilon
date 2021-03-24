class Polinomio:
    
    polinomio = []

    def __init__(self, value):
        self.polinomio = value

    def suma(self, otroPolinomio):

        # El tamaño del array solucion debe ser igual al más grande de los 2, mientras que solo se haran tantas iteraciones como el tamaño del más pequeño
        polinomioInverso = list(reversed(self.polinomio))
        otroPolinomioInverso = list(reversed(otroPolinomio))
        
        if len(self.polinomio) > len(otroPolinomio):
            solucion = polinomioInverso[:]
            for x in range(len(otroPolinomio)):
                solucion[x] += otroPolinomioInverso[x]
        else:
            solucion = otroPolinomioInverso[:]
            for x in range(len(self.polinomio)):
                solucion[x] += polinomioInverso[x]
        
        suma = Polinomio(list(reversed(solucion)))
        return suma

    def resta(self, otroPolinomio):

        otroPolinomioNegativo = otroPolinomio[:]

        for x in range(len(otroPolinomio)):
            otroPolinomioNegativo[x] *= -1

        resta = self.suma(otroPolinomioNegativo)

        return resta

    def producto(self, otroPolinomio):

        solucion = [0] * (len(self.polinomio) + len(otroPolinomio) - 1)

        for i in range(len(self.polinomio)):
            for j in range(len(otroPolinomio)):
                solucion[i + j] += self.polinomio[i] * otroPolinomio[j]
        producto = Polinomio(solucion)
        return producto

    def mcd(self):
        return True

    def to_string(self):

        resultado = ""
        longitud = len(self.polinomio)

        for i in range(longitud):
            if self.polinomio[i] > 0:
                resultado += str(self.polinomio[i])
            else:
                if self.polinomio[i] < 0:
                    resultado += str(self.polinomio[i] * -1)
                else:
                    continue

            if (i + 1) < longitud:
                resultado += "x^" + str(longitud - i - 1)
                if(self.polinomio[i + 1] > 0):
                    resultado += " + "
                else:
                    resultado += " - "

        return resultado
