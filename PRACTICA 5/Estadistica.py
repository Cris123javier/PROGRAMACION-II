import math

def obtener_numeros():
    while True:
        try:
            numeros = list(map(float, input("Ingrese 10 números separados por espacios: ").split()))
            if len(numeros) == 10:
                return numeros
            else:
                print("Error: Debe ingresar exactamente 10 números.")
        except ValueError:
            print("Error: Ingrese solo números válidos.")

def calcular_promedio(numeros):
     return sum(numeros) / len(numeros)

def calcular_desviacion(numeros, promedio):
    suma_diferencias = sum((x - promedio) ** 2 for x in numeros)
    return math.sqrt(suma_diferencias / (len(numeros) - 1))

def main():
    numeros = obtener_numeros()
    promedio = calcular_promedio(numeros)
    desviacion = calcular_desviacion(numeros, promedio)

    print(f"El promedio es {promedio:.2f}")
    print(f"La desviación estándar es {desviacion:.5f}")

# Funcion principal
if __name__ == "__main__":
    main()

