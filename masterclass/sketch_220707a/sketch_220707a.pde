
  size(1000,1000,P3D);


  background(0);
  
  color c = color(229, 204, 255);
  fill(c);
  noStroke();
  circle(200, 200, 300); // position x, y , r
  
  c = color(255, 204, 229);  // Update 'c' with grayscale value
  fill(c);  // Use updated 'c' as fill color
  circle(300, 350, 320);
  
  spotLight(204, 255, 255, 500/2, 250/2, 400, 0, 0, -1, 320/4, 2);
  circle(500, 250, 320);
  
  translate(300,600,100);
  rectMode(CENTER);
  rect(20,20,200,200);
    
