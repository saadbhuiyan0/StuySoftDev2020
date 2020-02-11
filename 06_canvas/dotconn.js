// Saad Bhuiyan
// SoftDev2 pd9
// K06 -- Canvas
// 2020-02-11


var c = document.getElementById("playground"); // retrieve canvas node in DOM via id
var ctx = c.getContext("2d"); // instantiate a CanvasRenderingctx2D object 
var cb = document.getElementById("clear"); // retrieve clear button via id

// vars used to hold x and y value of the last drawn dot
var lastX;
var lastY;

// function to draw dot and line to last point
var draw = function(e) {
    // vars used to hold x and y values for the new dot
    var newX = e.offsetX;
    var newY = e.offsetY;
    // draw a dot
    ctx.beginPath();
    ctx.arc(newX, newY, 10, 0, 2 * Math.PI);
    ctx.closePath();
    ctx.fill(); 
    // draw a line to the previous dot
    ctx.beginPath();
    ctx.moveTo(newX,newY);
    ctx.lineTo(lastX, lastY);
    ctx.stroke();
    ctx.closePath();
    // change coordinates of last dot to coordinates of new dot
    lastX = newX;
    lastY = newY;
    console.log("wow")
}

// function to clear the canvas
var clear = function(e) {
    ctx.clearRect(0, 0, c.width, c.height);
    lastX = undefined;
    lastY = undefined;
    console.log("poof");
}

// add event listeners for draw and clear
c.addEventListener("click", draw);
cb.addEventListener("click", clear);