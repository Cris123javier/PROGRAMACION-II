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
