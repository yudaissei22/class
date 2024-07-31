
class Phil implements Runnable{
    int x,y;
    int id;
    Fork left, right;

    public Phil(int id, int x, int y, Fork l, Fork r){
	this.id = id;
        this.x = x;
        this.y = y;
        this.left = left;
        this.right = right;
    }

    public void draw(){
	strokeWeight(10);
	if (left.owner == this) line(x, y, left.x, left.y);
	if (right.owner == this) line(x, y, right.x, right.y);
    }
    public void rsleep(int m){
	try{
	    Thread.sleep((int) random(m+100));
	}
	catch (Exception ex){
	}
    }

    public void sleep(int m){
	try {
	    Thread.sleep(m);
		}
	catch (Exception ex){
	}
    }

    public void run(){
	while (true){
	    rsleep(1500);
	    left.pick(this);
	    System.out.println("" + this.id + "picked left fork" + left.id);
	    rsleep(1000);
	    right.pick(this);
	    System.out.println("" + this.id + "picked right fork" + right.id);
	    rsleep(1000);
	    System.out.println("" + this.id + "drops right fork" + right.id);
	    right.drop(this);
	    System.out.println("" + this.id + "drops left fork" + left.id);
	    left.drop(this);
	}
    }
}

class Fork{
    int id;
    int x,y;
    Phil owner = null;

    public Fork(int id, int x, int y){
	this.id = id;
	this.x = x;
	this.y = y;
    }

    public synchronized void pick(Phil me) {
	while (owner != null){
	    // System.out.println("" + me.id + "waiting for Fork" + id + "from Phil:" + owner.id);
	    try{
		this.wait();
	    }
	    catch (Exception ex){
		System.out.println(ex);
	    }
	}
	owner = me;
    }

	public synchronized void drop(Phil me) {
		if (owner == me) {
		    owner = null;
		    this.notify();
		}
	    }
    }

