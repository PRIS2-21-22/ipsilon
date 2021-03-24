from polinomio import Polinomio

def main():

    valores1 = [1, 1, 4, 1]
    po1 = Polinomio(valores1)
    print("Polinomio 1: " + po1.toString())
    
    valores2 = [2, 2, -2, 2]
    po2 = Polinomio(valores2)
    print("Polinomio 2: " + po2.toString())

    suma = po1.suma(po2.polinomio)
    print("Suma  de los polinomios 1 y 2: " + suma.toString())
    
    resta = po1.resta(po2.polinomio)
    print("Resta de los polinomios 1 y 2: " + resta.toString())
    
    producto = po1.producto(po2.polinomio)
    print("Producto de los polinomios 1 y 2: " + producto.toString())

if __name__ == "__main__":
    main()