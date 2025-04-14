package PROGRAMACION_II;

public class A {
	protected int x;
    protected int z;
    
    public A(int x, int z) {
        this.x = x;
        this.z = z;
    }
    
    public void incrementaXZ() {
        this.x++;
        this.z++;
    }
    
    public void incrementaZ() {
        this.z++;
    }
    
    public int getX() {
        return x;
    }
    
    public int getZ() {
        return z;
    }
}
