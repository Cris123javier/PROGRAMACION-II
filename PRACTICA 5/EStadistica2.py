import math

class Estadisticas:
    def __init__(self, datos):
        self.datos = datos

    def promedio(self):
        return sum(self.datos) / len(self.datos)

    def desviacion(self):
        prom = self.promedio()
        suma_diferencias = sum((x - prom) ** 2 for x in self.datos)
        return math.sqrt(suma_diferencias / (len(self.datos) - 1))

# Entrada 
numeros = list(map(float, input("Ingrese 10 números separados por espacios: ").split()))

if len(numeros) == 10:
    stats = Estadisticas(numeros)
    print(f"El promedio es {stats.promedio():.2f}")
    print(f"La desviación estándar es {stats.desviacion():.5f}")
else:
    print("Debe ingresar exactamente 10 números.")

