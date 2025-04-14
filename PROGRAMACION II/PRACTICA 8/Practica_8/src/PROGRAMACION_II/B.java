package PROGRAMACION_II;

public class B {
	 protected int y;
	    protected int z;
	    
	    public B(int y, int z) {
	        this.y = y;
	        this.z = z;
	    }
	    
	    public void incrementaYZ() {
	        this.y++;
	        this.z++;
	    }
	    
	    public void incrementaZ() {
	        this.z++;
	    }
	    
	    public int getY() {
	        return y;
	    }
	    
	    public int getZ() {
	        return z;
	    }
}
