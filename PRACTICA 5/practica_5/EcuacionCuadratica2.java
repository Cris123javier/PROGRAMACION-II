package PRACTICA_5;

import java.util.Scanner;

class EcuacionCuadratica2 {
    private double a, b, c;
    
    public EcuacionCuadratica2(double a, double b, double c) {

        if(a == 0) {
            throw new IllegalArgumentException("El coeficiente 'a' no puede ser cero");
        }
        this.a = a;
        this.b = b;
        this.c = c;
    }
    
    public double getDiscriminante() {
        return (b * b) - (4 * a * c);
    }
    
    public Double getRaiz1() {
        double d = getDiscriminante();
        if (d >= 0) {
            return (-b + Math.sqrt(d)) / (2 * a);
        }
        return null;
    }
    
    public Double getRaiz2() {
        double d = getDiscriminante();
        if (d > 0) {
            return (-b - Math.sqrt(d)) / (2 * a);
        }
        return null;
    }
    
    public void resolver() {
        double d = getDiscriminante();
        
        if (d > 0) {
            System.out.printf("La ecuación tiene dos raíces:%n");
            System.out.printf("r₁ = %.5f%n", getRaiz1());
            System.out.printf("r₂ = %.5f%n", getRaiz2());
        } 
        else if (d == 0) {
            System.out.printf("La ecuación tiene una raíz:%n");
            System.out.printf("r = %.5f%n", getRaiz1());
        } 
        else {
            System.out.println("La ecuación no tiene raíces reales.");
        }
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        try {
            System.out.print("Ingrese el valor de a: ");
            double a = sc.nextDouble();
            
            System.out.print("Ingrese el valor de b: ");
            double b = sc.nextDouble();
            
            System.out.print("Ingrese el valor de c: ");
            double c = sc.nextDouble();
            
            EcuacionCuadratica2 ecuacion = new EcuacionCuadratica2(a, b, c);
            ecuacion.resolver();
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        } finally {
            sc.close();
        }
    }
}
