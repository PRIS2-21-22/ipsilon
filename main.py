from polinomio import Polinomio

def main():

    v1 = []

    n = int(input("Introduzca el grado del 1er polinomio: "))

    for _ in range(0, n):
        ele = int(input())

        v1.append(ele)

    print(v1)

    po1 = Polinomio(v1)

    v2 = []

    n = int(input("Introduzca el grado del 2do polinomio: "))

    for _ in range(0, n):
        ele = int(input())

        v2.append(ele)

    print(v2)
    po2 = Polinomio(v2)

    print("Polinomio 1: " + po1.to_string())
    print("Polinomio 2: " + po2.to_string())

    suma = po1.suma(po2.polinomio)
    print("Suma  de los polinomios 1 y 2: " + suma.to_string())

    resta = po1.resta(po2.polinomio)
    print("Resta de los polinomios 1 y 2: " + resta.to_string())

    producto = po1.producto(po2.polinomio)
    print("Producto de los polinomios 1 y 2: " + producto.to_string())

if __name__ == "__main__":
    main()