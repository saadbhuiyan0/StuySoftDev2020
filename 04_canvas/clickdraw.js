// Team CrosSaints - Benjamin Avrahami, Saad Bhuiyan, Kevin Cai
// SoftDev2 pd9
// K04 -- Canvas
// 2020-02-05

// retrieve node in DOM via ID
var c = document.getElementById("slate");

// instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

// setting Mona Lisa as canvas for ART
var imgPath = "monalisa.jpg";
var imgObj = new Image();
imgObj.src = imgPath;
imgObj.onload = function() {
    ctx.drawImage(imgObj, 65, 0);
}
console.log("Masterpiece completed.")

// current drawing mode
var currentMode = document.getElementById("mode");

// draw function to draw box or dot depending on mode
var draw = function(e) {
    if (currentMode.innerHTML == "Draw a Box") {
        ctx.fillStyle = "#FF00FF";
        ctx.fillRect(e.clientX, e.clientY, 33, 33);
    }
    else {
        ctx.fillStyle = "#8B008B";
        ctx.beginPath();
        ctx.arc(e.clientX, e.clientY, 20, 0, 2 * Math.PI, true);
        ctx.fill();
    }
}

// add event listener to canvas
c.addEventListener("click", draw);

// toggle drawing mode function
var toggleMode = function(e) {
    if (currentMode.innerHTML == "Draw a Box") {
        currentMode.innerHTML = "Draw a Dot";
        console.log("Changed drawing mode to: Draw a Dot.")
    }
    else {
        currentMode.innerHTML = "Draw a Box";
        console.log("Changed drawing mode to: Draw a Box.")
    }
}

// event listener to toggle drawing mode
var toggleButton = document.getElementById("toggle");
toggleButton.addEventListener("click", toggleMode);

// function to clear the canvas today
var clear = function(e) {
    ctx.clearRect(0, 0, c.width, c.height);
    console.log("You destroyed the Mona Lisa!");
}

// event listener for clearing canvas
var clearButton = document.getElementById("clear");
clearButton.addEventListener("click", clear);