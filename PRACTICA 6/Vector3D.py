import math

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, otro):
        return Vector3D(self.x + otro.x, self.y + otro.y, self.z + otro.z)
    
    def __mul__(self, escalar):
        if isinstance(escalar, (int, float)):
            return Vector3D(self.x * escalar, self.y * escalar, self.z * escalar)
        raise ValueError("el numero debe ser escalar")
    
    def __rmul__(self, escalar):
        return self.__mul__(escalar)
    
    def __truediv__(self, escalar):
        if escalar != 0:
            return Vector3D(self.x / escalar, self.y / escalar, self.z / escalar)
        raise ValueError("no se puede dividir por cero")
    
    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def normal(self):
        mag = self.magnitud()
        if mag == 0:
            raise ValueError("no se puede normalizar un vector cero")
        return self / mag
    
    def dot(self, otro):
        return self.x * otro.x + self.y * otro.y + self.z * otro.z
    
    def cross(self, otro):
        return Vector3D(
            self.y * otro.z - self.z * otro.y,
            self.z * otro.x - self.x * otro.z,
            self.x * otro.y - self.y * otro.x
        )
    
    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

# Ejemplo
a = Vector3D(2, 4, 6 )
b = Vector3D(4, 5, 6)
print("Suma:", a + b)
print("Multiplicación por escalar:", 2 * a)
print("Longitud de a:", a.magnitud())
print("Normalización de a:", a.normal())
print("Producto escalar:", a.dot(b))
print("Producto vectorial:", a.cross(b))
