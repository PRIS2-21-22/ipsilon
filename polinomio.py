class Polinomio:
    polinomio = []

    """Metodo constructor de la clase"""
    def __init__(self, value):
        self.polinomio = value

    def suma(self, other):

        # El tamaño del array solucion debe ser igual al más grande de los 2, mientras que solo se haran tantas iteraciones como el tamaño del más pequeño
        polinomio_inverso = list(reversed(self.polinomio))
        other_inverso = list(reversed(other))

        if len(self.polinomio) > len(other):
            solucion = polinomio_inverso[:]
            for x in range(len(other)):
                solucion[x] += other_inverso[x]
        else:
            solucion = other_inverso[:]
            for x in range(len(self.polinomio)):
                solucion[x] += polinomio_inverso[x]

        suma = Polinomio(list(reversed(solucion)))
        return suma

    def resta(self, other):

        other_negativo = other[:]

        for x in range(len(other)):
            other_negativo[x] *= -1

        resta = self.suma(other_negativo)

        return resta

    def producto(self, other):

        solucion = [0] * (len(self.polinomio) + len(other) - 1)

        for posi, val1 in enumerate(self.polinomio):
            for posj, val2 in enumerate(other):
                solucion[posi + posj] += val1 * val2
        producto = Polinomio(solucion)
        return producto

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
