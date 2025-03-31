import numpy as np

class AlgebraVectorial:
    def __init__(self, vector):
        self.vector = np.array(vector)
    
    def __add__(self, other):
        return AlgebraVectorial(self.vector + other.vector)
    
    def __sub__(self, other):
        return AlgebraVectorial(self.vector - other.vector)
    
    def __mul__(self, other):  # Producto punto
        return np.dot(self.vector, other.vector)
    
    def cruz(self, other):  # Producto cruz
        return np.cross(self.vector, other.vector)
    
    def es_perpendicular(self, other):
        return np.dot(self.vector, other.vector) == 0
    
    def es_paralelo(self, other):
        return np.allclose(np.cross(self.vector, other.vector), 0)
    
    def proyeccion_sobre(self, other):
        return (np.dot(self.vector, other.vector) / np.dot(other.vector, other.vector)) * other.vector
    
    def componente_en(self, other):
        return np.dot(self.vector, other.vector) / np.linalg.norm(other.vector)
    
    def norma(self):
        return np.linalg.norm(self.vector)
    
    def __str__(self):
        return str(self.vector)

def obtener_vector(mensaje):
    """Obtiene un vector desde el teclado con manejo de errores."""
    while True:
        try:
            entrada = input(f"{mensaje}: ")
            valores = [float(x.strip()) for x in entrada.split(',')]
            return AlgebraVectorial(valores)
        except ValueError:
            print("Error: Por favor ingrese números separados por comas (ejemplo: 1,2,3)")
        except Exception as e:
            print(f"Error inesperado: {e}")

def main():
    # Obtener los vectores del usuario
    print("\nIngrese las coordenadas del primer vector (x,y,z):")
    a = obtener_vector("Ingrese las coordenadas separadas por comas")
    
    print("\nIngrese las coordenadas del segundo vector (x,y,z):")
    b = obtener_vector("Ingrese las coordenadas separadas por comas")
    
    # Realizar operaciones y mostrar resultados
    print(f"\nVectores ingresados:")
    print(f"a = {a}")
    print(f"b = {b}")
    
    print(f"\n¿a y b son perpendiculares? {a.es_perpendicular(b)}")
    print(f"¿a y b son paralelos? {a.es_paralelo(b)}")
    
    if len(a.vector) == 3 and len(b.vector) == 3:
        producto_cruz = a.cruz(b)
        print(f"\nProducto cruz (a × b): {producto_cruz}")
    
    proyeccion = a.proyeccion_sobre(b)
    print(f"\nProyección de a sobre b: {proyeccion}")
    
    componente = a.componente_en(b)
    print(f"Componente de a en b: {componente}")

if __name__ == "__main__":
    main()