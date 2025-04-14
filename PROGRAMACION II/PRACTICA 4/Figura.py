import math

class FiguraGeometrica:
    
    def area(self, *args):
        if len(args) == 1:
            # Área de un círculo: π * r²
            radio = args[0]
            return math.pi * radio ** 2
        
        elif len(args) == 2:
            # Área de un rectángulo: base * altura
            base, altura = args
            return base * altura
        
        elif len(args) == 3:
            # Si el tercer argumento es True, es un triángulo rectángulo: (base * altura) / 2
            base, altura, es_triangulo = args
            if isinstance(es_triangulo, bool) and es_triangulo:
                return (base * altura) / 2
            else:
                return 0
        
        elif len(args) == 4:
            # Si el cuarto argumento es True, es un trapecio: ((baseMayor + baseMenor) * altura) / 2
            base_mayor, base_menor, altura, es_trapecio = args
            if isinstance(es_trapecio, bool) and es_trapecio:
                return ((base_mayor + base_menor) * altura) / 2
            else:
                return 0
        
        elif len(args) == 2 and args[1] == 6:
            # Área de un hexágono : (3√3/2) * lado²
            lado, es_hexagono = args
            return ((3 * math.sqrt(3)) / 2) * lado ** 2

        return 0  # En caso de parámetros incorrectos

# Pruebas
fig = FiguraGeometrica()

print("Círculo:", fig.area(5))  # Radio = 5
print("Rectángulo:", fig.area(4, 6))  # Base = 4, Altura = 6
print("Triángulo Rectángulo:", fig.area(3, 5, True))  # Base = 3, Altura = 5
print("Trapecio:", fig.area(6, 4, 5, True))  # Base Mayor = 6, Base Menor = 4, Altura = 5
print("Hexágono:", fig.area(4, 6))  # Lado = 4, Hexágono = 6 lados