// Saad Bhuiyan
// SoftDev2 pd9
// K12 -- Connect the Dots
// 2020-03-30


var svg = document.getElementById("playground"); 
var clear = document.getElementById("clear");

var lastX = null;
var lastY = null;
var clicked = false;

svg.addEventListener("click", function(e) {
    if (!clicked) {
        lastX = e.offsetX;
        lastY = e.offsetY;
        clicked = true;
    } 
    
    c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    c.setAttribute("cx", e.offsetX);
    c.setAttribute("cy", e.offsetY);
    c.setAttribute("r", 10);
    c.setAttribute("stroke", "blue");
    c.setAttribute("fill", "red");
    svg.appendChild(c);

    l = document.createElementNS("http://www.w3.org/2000/svg", "line");
    l.setAttribute("x1", lastX);
    l.setAttribute("y1", lastY);
    l.setAttribute("x2", e.offsetX);
    l.setAttribute("y2", e.offsetY);
    l.setAttribute("stroke", "black");
    svg.appendChild(l);
    
    lastX = e.offsetX;
    lastY = e.offsetY;
});
  
clear.addEventListener("click", function(e) {
    svg.innerHTML = "";
    lastX = null;
    lastY = null;
    clicked = false;
});