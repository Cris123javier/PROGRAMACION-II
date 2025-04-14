package PRACTICA_5;

import java.util.Scanner;

public class EcuacionCuadratica {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Ingrese el valor de a: ");
        double a = sc.nextDouble();
        
        while(a == 0) {
            System.out.println("Error: El coeficiente 'a' no puede ser cero.");
            System.out.print("Ingrese nuevamente el valor de a: ");
            a = sc.nextDouble();
        }
        
        System.out.print("Ingrese el valor de b: ");
        double b = sc.nextDouble();
        
        System.out.print("Ingrese el valor de c: ");
        double c = sc.nextDouble();
        
        double discriminante = (b * b) - (4 * a * c);
        
        if (discriminante > 0) {
            double r1 = (-b + Math.sqrt(discriminante)) / (2 * a);
            double r2 = (-b - Math.sqrt(discriminante)) / (2 * a);
            System.out.printf("La ecuación tiene dos raíces reales:%n");
            System.out.printf("r₁ = %.5f%n", r1);
            System.out.printf("r₂ = %.5f%n", r2);
        } 
        else if (discriminante == 0) {
            double r = -b / (2 * a);
            System.out.printf("La ecuación tiene una raíz real:%n");
            System.out.printf("r = %.5f%n", r);
        } 
        else {
            System.out.println("La ecuación no tiene raíces reales.");
        }
        
        sc.close();
    }
}

