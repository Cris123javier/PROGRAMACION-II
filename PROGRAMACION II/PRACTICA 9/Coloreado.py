import tkinter as tk
from abc import ABC, abstractmethod
import random
import math

class Coloreado(ABC):
    @abstractmethod
    def comoColorear(self):
        pass

class Figura(ABC):
    def __init__(self, color="sin color"):
        self.color = color
    
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def __str__(self):
        return f"Color: {self.color}"
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

class Cuadrado(Figura, Coloreado):
    def __init__(self, lado, color="sin color"):
        super().__init__(color)
        self.lado = lado
    
    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        return 4 * self.lado
    
    def comoColorear(self):
        return "Colorear los cuatro lados"

class Circulo(Figura):
    def __init__(self, radio, color="sin color"):
        super().__init__(color)
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio

class SistemaFiguras(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Sistema de Figuras Geométricas")
        self.geometry("800x600")
        self.configure(bg='#39ff33')
        
        self.canvas = tk.Canvas(self, width=600, height=400, bg='white')
        self.canvas.pack(pady=20)
        
        self.text_area = tk.Text(self, height=10, width=60)
        self.text_area.pack(pady=10)
        
        self.generar_figuras()
    
    def dibujar_cuadrado(self, cuadrado, x, y):
        lado = cuadrado.lado * 20  # Escala para visualización
        self.canvas.create_rectangle(
            x, y,
            x + lado, y + lado,
            fill=cuadrado.color,
            outline='black'
        )
    
    def dibujar_circulo(self, circulo, x, y):
        radio = circulo.radio * 20  # Escala para visualización
        self.canvas.create_oval(
            x, y,
            x + radio*2, y + radio*2,
            fill=circulo.color,
            outline='black'
        )
    
    def generar_figuras(self):
        figuras = []
        for _ in range(5):
            tipo = random.randint(1, 2)
            if tipo == 1:
                lado = random.randint(1, 10)
                cuadrado = Cuadrado(lado, "red")
                figuras.append(cuadrado)
            else:
                radio = random.randint(1, 10)
                circulo = Circulo(radio, "blue")
                figuras.append(circulo)
        
        # Dibujar las figuras
        x = 50
        y = 50
        for figura in figuras:
            if isinstance(figura, Cuadrado):
                self.dibujar_cuadrado(figura, x, y)
            else:
                self.dibujar_circulo(figura, x, y)
            x += 150
            if x > 500:
                x = 50
                y += 150
        
        # Mostrar información
        self.text_area.delete(1.0, tk.END)
        for i, figura in enumerate(figuras, 1):
            self.text_area.insert(tk.END, f"\nFigura {i}:\n")
            self.text_area.insert(tk.END, str(figura) + "\n")
            self.text_area.insert(tk.END, f"Área: {figura.area():.2f}\n")
            self.text_area.insert(tk.END, f"Perímetro: {figura.perimetro():.2f}\n")
            if isinstance(figura, Coloreado):
                self.text_area.insert(tk.END, f"Cómo colorear: {figura.comoColorear()}\n")
            self.text_area.insert(tk.END, "-" * 40 + "\n")

if __name__ == "__main__":
    app = SistemaFiguras()
    app.mainloop()
