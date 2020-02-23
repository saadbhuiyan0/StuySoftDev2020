// Saad Bhuiyan
// SoftDev2 pd9
// K08 -- Canvas Animation
// 2020-02-23


var c = document.getElementById("playground"); // retrieve canvas node in DOM via id
var ctx = c.getContext("2d"); // instantiate a CanvasRenderingctx2D object 

var r = 20;
var grow = true;
var id = 0;

var logo = new Image();
logo.src = "https://raw.githubusercontent.com/stuy-softdev/notes-and-code19-20/master/smpl/200214f_js-canvas-anim/logo_dvd.jpg?token=AKILQI5PXMXRQUU7A3MIV3C6J4EPM";

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
  
var xpos;
var ypos;
var right = true;
var down = true;
var dvid = 0;

var bounce = function(e) {
    ctx.drawImage(logo,xpos,ypos,60,30);
    if (right) {
        xpos++;
        if (xpos+60 == c.width) {
            right = false;
        }
    }
    else {
        xpos--;
        if (xpos == 0) {
            right = true;
        }
    }
    if (down) {
        ypos++;
        if (ypos+30 == c.height) {
            down = false;
        }
    }
    else {
        ypos--;
        if (ypos == 0) {
            down = true;
        }
    }
    dvid = requestAnimationFrame(bounce);
}

var go = document.getElementById("anim");
var begin = function(e) {
    end();
    go.removeEventListener("click",begin);
    draw();
}
go.addEventListener("click",begin);

var con = document.getElementById("dvd");
var mid = function(e) {
    end();
    ctx.clearRect(0,0,c.width,c.height);
    con.removeEventListener("click",mid);
    bounce();
}
var reloc = function(e) {
    ctx.clearRect(0,0,c.width,c.height);
    xpos = Math.floor((c.width-60) * Math.random());
    ypos = Math.floor((c.height-30) * Math.random());
}
con.addEventListener("click",mid);
con.addEventListener("click",reloc);

var stop = document.getElementById("stop");
var end = function(e) {
    window.cancelAnimationFrame(id);
    window.cancelAnimationFrame(dvid);
    go.addEventListener("click",begin);
    con.addEventListener("click",mid);
}
stop.addEventListener("click",end);