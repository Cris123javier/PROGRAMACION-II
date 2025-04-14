import random

class Juego:
    def __init__(self, numeroDeVidas, record):
        self.numeroDeVidas = numeroDeVidas
        self.record = record
    
    def reiniciaPartida(self):
        self.numeroDeVidas = 3  
    
    def actualizaRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas
        print(f"Record actualizado a: {self.record}")
    
    def quitaVida(self):
        self.numeroDeVidas -= 1
        if self.numeroDeVidas > 0:
            return True
        else:
            return False

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas, 0)
        self.numeroAAdivinar = random.randint(0, 10)
    
    def obtenerEntradaValida(self):
        """Obtiene una entrada válida del usuario."""
        while True:
            try:
                entrada = input("Adivina un número entre 0 y 10: ")
                numero = int(entrada)
                if 0 <= numero <= 10:
                    return numero
                else:
                    print("El número debe estar entre 0 y 10.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

    def juega(self):
        self.reiniciaPartida()
        print("Bienvenido al juego de adivinar el número!")
        
        while self.numeroDeVidas > 0:
            adivinanza = self.obtenerEntradaValida()

            if adivinanza == self.numeroAAdivinar:
                print("¡Acertaste!")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if adivinanza < self.numeroAAdivinar:
                        print("El número es mayor. Intenta de nuevo.")
                    else:
                        print("El número es menor. Intenta de nuevo.")
                else:
                    print("¡Se te han acabado las vidas! Fin del juego.")
                    break

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def obtenerEntradaValida(self):
        """Obtiene una entrada válida del usuario para números pares."""
        while True:
            numero = super().obtenerEntradaValida()
            if numero % 2 == 0:
                return numero
            else:
                print("El número debe ser par.")

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def obtenerEntradaValida(self):
        """Obtiene una entrada válida del usuario para números impares."""
        while True:
            numero = super().obtenerEntradaValida()
            if numero % 2 != 0:
                return numero
            else:
                print("El número debe ser impar.")

class Aplicacion:
    def main(self):
        print("=== JUEGO ADIVINA NÚMERO ===")
        juego1 = JuegoAdivinaNumero(3)
        juego1.juega()
        
        print("\n=== JUEGO ADIVINA PAR ===")
        juego2 = JuegoAdivinaPar(3)
        juego2.juega()
        
        print("\n=== JUEGO ADIVINA IMPAR ===")
        juego3 = JuegoAdivinaImpar(3)
        juego3.juega()

# Ejecucion del programa
if __name__ == "__main__":
    aplicacion = Aplicacion()
    aplicacion.main()
