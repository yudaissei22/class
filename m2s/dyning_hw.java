class Phil implements Runnable{
    String name;
    Fork left, right;

    public Phil(String name, Fork l, Fork r){
	this.name = name;
	this.left = l;
	this.right = r;	    
    }

    public void run(){
	while(true){
	    sleep();
	    left.pick(this)
	    sleep();
	    right.pick(this)
	    sleep();
	    left.drop(this)
	    sleep();
	    right.drop(this)		
	}
    }
    
}


class Fork{
    String name;
    Phil owner = null;
    public Fork(String name){
	this.name = name;
    }

    public synchronized void pick(Phil me){
	while (owner != null){
	    try{
		this.wait();
	    } catch (Exception ex) {}
	}
	owner = me;
	println(me.name + "picks up" + name);
    }

    public synchronized void drop(Phil me){
	if (owner == me){
	    owner == null;
	    println(me.name + "drops" + name);
	    this.notify();
	}
    }
}
