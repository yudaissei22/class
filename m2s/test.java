void setup(){
  size(500,500);
}

void draw(){
  strokeWeight(random(3,6));
  stroke(random(0,255), random(0,255), random(0,255), 100);
  line(random(0,500), random(0,500), random(0,500), random(0,500));
}
