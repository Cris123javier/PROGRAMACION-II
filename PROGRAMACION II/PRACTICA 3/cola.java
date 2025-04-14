public class Main {
    public static void main(String[] args) {
        System.out.println("=== PRUEBA DE PILA ===");
        Pila pila = new Pila(5);
        pila.push(10);
        pila.push(20);
        pila.push(30);
        System.out.println("Cima de la pila: " + pila.peek());
        System.out.println("Se extrae: " + pila.pop());
        System.out.println("¿Está vacía? " + pila.isEmpty());
        System.out.println("¿Está llena? " + pila.isFull());

        System.out.println("\n=== PRUEBA DE COLA ===");
        Cola cola = new Cola(5);
        cola.insert(100);
        cola.insert(200);
        cola.insert(300);
        System.out.println("Frente de la cola: " + cola.peek());
        System.out.println("Se extrae: " + cola.remove());
        System.out.println("Tamaño actual: " + cola.size());
        System.out.println("¿Está vacía? " + cola.isEmpty());
        System.out.println("¿Está llena? " + cola.isFull());
    }
}

// ----------------------- CLASE PILA -----------------------
class Pila {
    private long[] arreglo;
    private int top;
    private int n;

    public Pila(int n) {
        this.n = n;
        this.arreglo = new long[n];
        this.top = -1;
    }

    public void push(long e) {
        if (!isFull()) {
            arreglo[++top] = e;
        } else {
            System.out.println("Pila llena");
        }
    }

    public long pop() {
        if (!isEmpty()) {
            return arreglo[top--];
        }
        System.out.println("Pila vacía");
        return -1;
    }

    public long peek() {
        if (!isEmpty()) {
            return arreglo[top];
        }
        System.out.println("Pila vacía");
        return -1;
    }

    public boolean isEmpty() {
        return top == -1;
    }

    public boolean isFull() {
        return top == n - 1;
    }
}