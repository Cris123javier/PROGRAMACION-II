import math

a, b, c = map(float, input("Ingrese a, b, c: ").split())

# Cálculo del discriminante
discriminante = b**2 - 4*a*c

if discriminante > 0:
    r1 = (-b + math.sqrt(discriminante)) / (2*a)
    r2 = (-b - math.sqrt(discriminante)) / (2*a)
    print(f"La ecuación tiene dos raíces {r1:.5f} y {r2:.5f}")
elif discriminante == 0:
    r1 = -b / (2*a)
    print(f"La ecuación tiene una raíz {r1:.5f}")
else:
    print("La ecuación no tiene raíces reales")

