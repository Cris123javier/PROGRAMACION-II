import tkinter as tk
from tkinter import ttk, messagebox
from abc import ABC, abstractmethod

class Boleto(ABC):
    def __init__(self, numero_boleto):
        self.numero_boleto = numero_boleto
        self.precio = 0.0
    
    @abstractmethod
    def calcular_precio(self):
        pass
        
    def __str__(self):
        return f"Número: {self.numero_boleto}, Precio: ${self.precio}"

class Palco(Boleto):
    def __init__(self, numero_boleto):
        super().__init__(numero_boleto)
        self.precio = 100.0
    
    def calcular_precio(self):
        return self.precio

class Platea(Boleto):
    def __init__(self, numero_boleto, dias_anticipacion):
        super().__init__(numero_boleto)
        if dias_anticipacion >= 10:
            self.precio = 50.0
        else:
            self.precio = 60.0
    
    def calcular_precio(self):
        return self.precio

class Galeria(Boleto):
    def __init__(self, numero_boleto, dias_anticipacion):
        super().__init__(numero_boleto)
        if dias_anticipacion >= 10:
            self.precio = 25.0
        else:
            self.precio = 30.0
    
    def calcular_precio(self):
        return self.precio

class SistemaVentasBoletos(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Sistema de Ventas de Boletos")
        self.geometry("400x500")
        self.configure(bg='#f0f0f0')
        
        # Variables para los campos de entrada
        self.numero_boleto = tk.StringVar()
        self.dias_anticipacion = tk.StringVar()
        self.tipo_boleto = tk.StringVar(value="Palco")
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Título principal
        titulo = ttk.Label(
            self,
            text="Teatro Municipal",
            font=("Arial", 16, "bold"),
            background='#f0f0f0'
        )
        titulo.pack(pady=20)
        
        # Frame para selección de tipo de boleto
        frame_tipo = ttk.LabelFrame(
            self,
            text="Tipo de Boleto",
            padding="10"
        )
        frame_tipo.pack(fill="x", padx=20, pady=5)
        
        tipos = ["Palco", "Platea", "Galería"]
        for tipo in tipos:
            ttk.Radiobutton(
                frame_tipo,
                text=tipo,
                value=tipo,
                variable=self.tipo_boleto,
                command=self.actualizar_interfaz
            ).pack(anchor="w")
        
        # Frame para entrada de número de boleto
        frame_numero = ttk.LabelFrame(
            self,
            text="Número de Boleto",
            padding="10"
        )
        frame_numero.pack(fill="x", padx=20, pady=5)
        
        ttk.Entry(
            frame_numero,
            textvariable=self.numero_boleto,
            width=20
        ).pack(pady=5)
        
        # Frame para días de anticipación
        self.frame_dias = ttk.LabelFrame(
            self,
            text="Días de Anticipación",
            padding="10"
        )
        self.frame_dias.pack(fill="x", padx=20, pady=4)
        
        ttk.Entry(
            self.frame_dias,
            textvariable=self.dias_anticipacion,
            width=20
        ).pack(pady=2)
        
        # Botón de compra
        ttk.Button(
            self,
            text="Comprar Boleto",
            command=self.comprar_boleto
        ).pack(pady=20)
        
        # Resultado
        self.resultado = tk.Text(
            self,
            height=5,
            width=40,
            bg='#f0f0f0'
        )
        self.resultado.pack(padx=20, pady=10)
        
        self.actualizar_interfaz()
    
    def actualizar_interfaz(self):
        tipo = self.tipo_boleto.get()
        if tipo == "Palco":
            self.frame_dias.pack_forget()
        else:
            self.frame_dias.pack(fill="x", padx=20, pady=5)
    
    def comprar_boleto(self):
        try:
            numero = int(self.numero_boleto.get())
            
            if self.tipo_boleto.get() == "Palco":
                boleto = Palco(numero)
            else:
                dias = int(self.dias_anticipacion.get())
                if self.tipo_boleto.get() == "Platea":
                    boleto = Platea(numero, dias)
                else:
                    boleto = Galeria(numero, dias)
            
            self.resultado.delete(1.0, tk.END)
            self.resultado.insert(tk.END, str(boleto))
            
        except ValueError:
            messagebox.showerror(
                "Error",
                "Por favor ingrese valores numéricos válidos"
            )
    
    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = SistemaVentasBoletos()
    app.run()
