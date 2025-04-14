package PROGRAMACION_II;

public class D extends A {
	private B b;
    private int y;
    
    public D(int x, int y, int z) {
        super(x, z);
        this.b = new B(y, z);
        this.y = y;
    }
    
    public void incrementaXYZ() {
        this.x++;
        this.y++;
        this.z++;
    }
    
    public void incrementaYZ() {
        b.incrementaYZ();
        this.y = b.getY();
        this.z = b.getZ();
    }
    
    @Override
    public void incrementaZ() {
        super.incrementaZ();
        b.incrementaZ();
        this.z = super.getZ();
    }
    
    public int getY() {
        return y;
    }
}
