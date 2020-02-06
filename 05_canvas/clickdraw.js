// Saad Bhuiyan
// SoftDev2 pd9
// K05 -- Canvas
// 2020-02-06

// retrieve node in DOM via ID
var c = document.getElementById("slate");

// instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

// setting Mona Lisa as canvas for ART
var imgPath = "monalisa.jpg";
var imgObj = new Image(); // insantiate an image object
imgObj.src = imgPath; // set the source for the image object as 
imgObj.onload = function() {
    ctx.drawImage(imgObj, 65, 0); // draw the image onto the canvas on load
}
console.log("Masterpiece completed.")

// drawing mode starts as box because HTML page loads up in Draw-a-Rectangle mode
var currentMode = "box";

// draw function to draw box or dot depending on mode
var draw = function(e) {
    // changed the x y inputs for drawing shapes from clientX and clientY to offsetX and offsetY
    // offsetX and offsetY are relative to the parent container - the canvas
    // whereas clientX and clientY were coordinates according to the client and caused an offset in the canvas
    // if the mode is in box draw a magenta rectangle at user mouse input
    if (currentMode == "box") {
        ctx.fillStyle = "#FF00FF";
        ctx.fillRect(e.offsetX, e.offsetY, 33, 33);
    }
    // if the mode is in dot draw a dark purple dot centered at user mouse input
    else {
        ctx.fillStyle = "#8B008B";
        ctx.beginPath(); // beginPath essentially puts the pen down for a path on the canvas, necessary for arc
        ctx.arc(e.offsetX, e.offsetY, 20, 0, 2 * Math.PI, true); // using the pen draw an arc (full 360) centered at mouse input
        ctx.fill(); // fill the dot with purple for visibility
    }
}

// add event listener to canvas
c.addEventListener("click", draw);

// toggle drawing mode function will change variable value and what is shown in HTML
var toggleMode = function(e) {
    if (currentMode == "box") {
        currentMode = "dot";
        document.getElementById("mode").innerHTML = "Draw-a-Dot";
        console.log("Changed drawing mode to: Draw-a-Dot.")
    }
    else {
        currentMode = "box";
        document.getElementById("mode").innerHTML = "Draw-a-Rectangle";
        console.log("Changed drawing mode to: Draw-a-Rectangle.")
    }
    e.preventDefault();
}

// event listener to toggle drawing mode
var toggleButton = document.getElementById("toggle");
toggleButton.addEventListener("click", toggleMode);

// function to clear the canvas today
var clear = function(e) {
    // e.preventDefault(); 
    // could not figure out what e.preventDefault() does after experimentation
    // from the documentation I understand when an event is not handled, the function should not have an effect
    ctx.clearRect(0, 0, c.width, c.height);
    console.log("You destroyed the Mona Lisa!");
}

// event listener for clearing canvas
var clearButton = document.getElementById("clear");
clearButton.addEventListener("click", clear);