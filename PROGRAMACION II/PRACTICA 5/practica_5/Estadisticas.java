package PRACTICA_5;

import java.util.Scanner;
import java.util.InputMismatchException;

class Estadisticas {
    private double[] datos;
    
    public Estadisticas(double[] datos) {
        if (datos == null || datos.length == 0) {
            throw new IllegalArgumentException("El array de datos no puede ser nulo o vacío");
        }
        this.datos = datos;
    }
    
    public double promedio() {
        double suma = 0;
        for (double num : datos) {
            suma += num;
        }
        return suma / datos.length;
    }
    
    public double desviacion() {
        if (datos.length < 2) {
            throw new IllegalArgumentException("Se necesitan al menos 2 datos para calcular la desviación estándar");
        }
        double prom = promedio();
        double sumaDiferencias = 0;
        for (double num : datos) {
            sumaDiferencias += Math.pow(num - prom, 2);
        }
        return Math.sqrt(sumaDiferencias / (datos.length - 1));
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            System.out.println("Ingrese 10 números separados por espacios (puede usar decimales con punto):");
            double[] numeros = new double[10];
            
            for (int i = 0; i < 10; i++) {
                boolean valido = false;
                while (!valido) {
                    try {
                        System.out.printf("Número %d: ", i + 1);
                        numeros[i] = sc.nextDouble();
                        valido = true;
                    } catch (InputMismatchException e) {
                        System.out.println("Error: Por favor ingrese un número válido (use punto para decimales)");
                        sc.next(); // Limpiar el buffer de entrada
                    }
                }
            }
            
            Estadisticas stats = new Estadisticas(numeros);
            System.out.printf("El promedio es %.2f%n", stats.promedio());
            System.out.printf("La desviación estándar es %.5f%n", stats.desviacion());
            
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            sc.close();
        }
    }
}
