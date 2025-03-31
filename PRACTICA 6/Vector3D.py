import math

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)
        raise ValueError("Scalar must be a number")
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        if scalar != 0:
            return Vector3D(self.x / scalar, self.y / scalar, self.z / scalar)
        raise ValueError("Cannot divide by zero")
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return self / mag
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

# Ejemplo
a = Vector3D(2, 4, 6 )
b = Vector3D(4, 5, 6)
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación por escalar:", 2 * a)
print("Longitud de a:", a.magnitude())
print("Normalización de a:", a.normalize())
print("Producto escalar:", a.dot(b))
print("Producto vectorial:", a.cross(b))
