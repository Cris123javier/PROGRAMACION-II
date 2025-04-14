package PRACTICA_5;

import java.util.Scanner;
import java.util.InputMismatchException;

public class Estadistica {
    public static double[] obtenerNumeros() {
        Scanner sc = new Scanner(System.in);
        double[] numeros = new double[10];
        
        while (true) {
            System.out.println("Ingrese 10 números separados por espacios (puede usar decimales con coma):");
            boolean entradaValida = true;
            
            for (int i = 0; i < 10; i++) {
                try {
                    System.out.printf("Número %d: ", i + 1);
                    numeros[i] = sc.nextDouble();
                } catch (InputMismatchException e) {
                    entradaValida = false;
                    System.out.println("Error: Por favor ingrese un número válido (use coma para decimales)");
                    sc.next(); 
                    break;
                }
            }
            
            if (entradaValida) {
                return numeros;
            } else {
                System.out.println("Error: Ingrese exactamente 10 números válidos.");
                sc.nextLine(); 
            }
        }
    }
    
    public static double calcularPromedio(double[] numeros) {
        double suma = 0;
        for (double num : numeros) {
            suma += num;
        }
        return suma / numeros.length;
    }
    
    public static double calcularDesviacion(double[] numeros, double promedio) {
        if (numeros.length < 2) {
            throw new IllegalArgumentException("Se necesitan al menos 2 datos para calcular la desviación estándar");
        }
        double sumaDiferencias = 0;
        for (double num : numeros) {
            sumaDiferencias += Math.pow(num - promedio, 2);
        }
        return Math.sqrt(sumaDiferencias / (numeros.length - 1));
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            double[] numeros = obtenerNumeros();
            double promedio = calcularPromedio(numeros);
            double desviacion = calcularDesviacion(numeros, promedio);
            System.out.printf("El promedio es %.2f%n", promedio);
            System.out.printf("La desviación estándar es %.5f%n", desviacion);
            
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            sc.close();
        }
    }
}
