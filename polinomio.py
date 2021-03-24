class Polinomio:
    
    polinomio = []

    def __init__(self, value):
        self.polinomio = value

    def suma(self, otro_polinomio):

        # El tamaño del array solucion debe ser igual al más grande de los 2, mientras que solo se haran tantas iteraciones como el tamaño del más pequeño
        polinomio_inverso = list(reversed(self.polinomio))
        otro_polinomio_inverso = list(reversed(otro_polinomio))
        
        if len(self.polinomio) > len(otro_polinomio):
            solucion = polinomio_inverso[:]
            for x in range(len(otro_polinomio)):
                solucion[x] += otro_polinomio_inverso[x]
        else:
            solucion = otro_polinomio_inverso[:]
            for x in range(len(self.polinomio)):
                solucion[x] += polinomio_inverso[x]
        
        suma = Polinomio(list(reversed(solucion)))
        return suma

    def resta(self, otroPolinomio):

        otro_polinomio_negativo = otroPolinomio[:]

        for x in range(len(otroPolinomio)):
            otro_polinomio_negativo[x] *= -1

        resta = self.suma(otro_polinomio_negativo)

        return resta

    def producto(self, otro_polinomio):

        solucion = [0] * (len(self.polinomio) + len(otro_polinomio) - 1)

        for i in range(len(self.polinomio)):
            for j in range(len(otro_polinomio)):
                solucion[i + j] += self.polinomio[i] * otro_polinomio[j]
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
