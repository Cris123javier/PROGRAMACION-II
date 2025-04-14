package Programacion;

public class FiguraGeometrica {
    
    // Área de un círculo
    double area(double radio) {
        return Math.PI * radio * radio;
    }

    // Área de un rectángulo
    double area(double base, double altura) {
        return base * altura;
    }

    // Área de un triángulo rectángulo
    double area(double base, double altura, boolean esTriangulo) {
        if (esTriangulo) {
            return (base * altura) / 2;
        }
        return 0; 
    }

    // Área de un trapecio
    double area(double baseMayor, double baseMenor, double altura, boolean esTrapecio) {
        if (esTrapecio) {
            return ((baseMayor + baseMenor) * altura) / 2;
        }
        return 0; // En caso de que no sea un trapecio
    }

    // Área de un hexágono 
    double area(double lado, int esHexagono) {
        if (esHexagono == 6) { // 6 indica que es un hexágono
            return ((3 * Math.sqrt(3)) / 2) * lado * lado;
        }
        return 0; // En caso de que no sea un hexágono
    }

    public static void main(String[] args) {
        FiguraGeometrica fig = new FiguraGeometrica();

        System.out.println("Círculo: " + fig.area(5)); // Radio = 5
        System.out.println("Rectángulo: " + fig.area(4, 6)); // Base = 4, Altura = 6
        System.out.println("Triángulo Rectángulo: " + fig.area(3, 5, true)); // Base = 3, Altura = 5
        System.out.println("Trapecio: " + fig.area(6, 4, 5, true)); // Base Mayor = 6, Base Menor = 4, Altura = 5
        System.out.println("Hexágono: " + fig.area(4, 6)); // Lado = 4, Hexágono = 6 lados
    }
}