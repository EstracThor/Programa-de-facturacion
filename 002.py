# Validaciones -> comprobar que los números ingresados 
# sean positivos comprobar que sean números
def suma(a, b):
    return a + b

def pedir_numero():
    while True:
        try:
            numero = float(input("Ingresa un número positivo: "))

            if numero > 0:
                return numero
            else:
                print("Error: El número debe ser positivo.")

        except ValueError:
            print("Error: Ingresa solo números.")

n1 = pedir_numero()
n2 = pedir_numero()

resultado = suma(n1, n2)
print("La suma es:", resultado)
