// Saad Bhuiyan
// SoftDev2 pd9
// K07 -- Canvas Animation
// 2020-02-12


var c = document.getElementById("playground"); // retrieve canvas node in DOM via id
var ctx = c.getContext("2d"); // instantiate a CanvasRenderingctx2D object 
var ab = document.getElementById("start"); // retrieve animate button via id
var sb = document.getElementById("stop"); // retrieve stop button via id

// canvas center
var centerX = c.width/2
var centerY = c.height/2

// function to start the animation
var start = function() {
    window.cancelAnimationFrame(animate);
}

// function to animate a circle growing and shrinking
var animate = function() {
    console.log(centerX);
    var radius = 10;
    ctx.beginPath();
    ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI);
    ctx.closePath();
    ctx.fill();
}

// function to stop the animation
var stop = function() {
    window.cancelAnimationFrame(animate);
}

// add event listeners to start and stop
ab.addEventListener("start", start);
sb.addEventListener("stop", stop);