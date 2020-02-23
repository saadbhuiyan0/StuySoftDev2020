// Saad Bhuiyan
// SoftDev2 pd9
// K07 -- Canvas Animation
// 2020-02-12


var c = document.getElementById("playground"); // retrieve canvas node in DOM via id
var ctx = c.getContext("2d"); // instantiate a CanvasRenderingctx2D object 

var r = 20;
var grow = true;
var id = 0;

var draw = function(e) {
    ctx.clearRect(0,0,c.width,c.height);
    ctx.beginPath();
    ctx.arc(c.width/2, c.height/2, r, 0, 2 * Math.PI, true);
    ctx.fill();
    if (grow) {
        r += 1;
        if (r == Math.min(c.height,c.width)/2) {
            grow = false;
        }
    }
    else {
        r -= 1;
        if (r == 0) {
            grow = true;
        }
    }
    id = window.requestAnimationFrame(draw);
}
  
var go = document.getElementById("anim");
var begin = function(e) {
    window.requestAnimationFrame(draw);
    go.removeEventListener("click",begin);
}
go.addEventListener("click",begin);
  
var stop = document.getElementById("stop");
var end = function(e) {
    window.cancelAnimationFrame(id);
    go.addEventListener("click",begin);
}
stop.addEventListener("click",end);