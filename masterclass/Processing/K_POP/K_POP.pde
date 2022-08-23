color yellow = color(255, 233, 96);
color purple = color(190, 170, 255);
color pink = color(255, 166, 220);
color blue = color(127, 150, 251);
color white = color(255, 255, 255);

/**
 * Pie Chart  
 * 
 * Uses the arc() function to generate a pie chart from the data
 * stored in an array. 
 */

int[] angles = { 342, 15, 3 };

void setup() {
  size(640, 360);
  noStroke();
  noLoop();  // Run once and stop
}

void draw() {
  background(100);
  pieChart(300, angles);
}

void pieChart(float diameter, int[] data) {
  float lastAngle = 0;
  for (int i = 0; i < data.length; i++) {
    if(i==0) fill(pink);
    if(i==1) fill(blue);
    if(i==2) fill(purple);
    arc(width/2, height/2, diameter, diameter, lastAngle, lastAngle+radians(data[i]));
    lastAngle += radians(data[i]);
  }
}
