/*
Justin Chen and Saad Bhuiyan
SoftDev2 pd02 and pd09
K18 -- Come Up For Air
2020-04-21

Helpful:
    https://bl.ocks.org/d3noob/402dd382a51a4f6eea487f9a35566de0
    https://www.d3-graph-gallery.com/graph/line_basic.html
    https://www.dashingd3js.com/svg-paths-and-d3js
*/

// Get json data
var data;

fetch("/data")
    // Get the json data
    .then((response) => {
        return response.json();
    })
    // store the data in a variable
    .then((returnedJSON) => {
        data = returnedJSON["data"];
    });

// Variables
var svg, xAxis, yAxis;
var loaded = false;
var done = false;
var counter = 1;
var frameCounter = 0;

// Buttons
var loadButton = document.getElementById("load");
loadButton.addEventListener("click", load);

var animButton = document.getElementById("anim");
animButton.addEventListener("click", anim);

// Helper functions for getting data into proper format
function getYears(start, end) {
    var years = [];
    var index = 0;

    for (i = start; i <= end; i++) {
        // Parse integer to year
        var format = d3.timeParse(("%Y"));
        years[index++] = format(i + 1880);
    }

    return years;
}

function getAnomalies(start, end) {
    var anomalies = [];
    var index = 0;

    for (i = start; i <= end; i++) {
        anomalies[index++] = parseFloat(data[i + 1880]);
    }

    return anomalies;
}

function createDataObject(years, anomalies) {
    var dataObject = [];

    for (i = 0; i <= 1; i++) {
        dataObject[i] = {
            "year": years[i],
            "anom": anomalies[i]
        };
    }
    return dataObject;
}

// Create the SVG and graph
function drawGraph() {
    // Variables
    var svgHeight = 600;
    var svgWidth = 600;

    var margins = { top: 50, bottom: 50, left: 50, right: 50 };
    var height = svgHeight - margins.top - margins.bottom;
    var width = svgWidth - margins.left - margins.right;

    var years = getYears(0, 136);
    var anomalies = getAnomalies(0, 136);

    // Create SVG
    svg = d3.select("#svg")
        .append("svg")
        .attr("height", svgHeight)
        .attr("width", svgWidth)
        .append("g")
        .attr("transform", "translate(" + margins.left + "," + margins.top + ")");

    // Set axes
    // Domain: min, max of our values
    // Range: size of our graph
    xAxis = d3.scaleTime()
        .domain(d3.extent(years))
        .range([0, width]);
    yAxis = d3.scaleLinear()
        .domain(d3.extent(anomalies))
        // Height on top, 0 on bottom
        .range([height, 0]);
    // Label yAxis
    svg.append("text")
    .attr("transform", "rotate(-90)")
    .attr("x", 0 - svgHeight / 2)
    .attr("y", 0 - margins.left * .75)
    .text("Degrees Celsius");

    // Add axes to SVG
    svg.append("g")
        // Move x-axis to middle
        .attr("transform", "translate(0," + height / 2 + ")")
        .call(d3.axisBottom(xAxis));
    svg.append("g").call(d3.axisLeft(yAxis));
}

function drawLine(n) {
    // Only draw a line segment
    var years = getYears(n - 1, n);
    var anomalies = getAnomalies(n - 1, n);
    var myData = createDataObject(years, anomalies);

    // Generate the line's path
    var line = d3.line()
        // Set x/y values to that in years/anomalies
        .x(d => xAxis(d.year))
        .y(d => yAxis(d.anom));

    // Add the line
    svg.append("path")
        .attr("stroke", "red")
        .attr("fill", "none")
        .attr("stroke-width", 1.5)
        // Pass data to line generator
        .attr("d", line(myData));
}

function load(e) {
    // Load and reset after animation
    if (!loaded) {
        d3.select("svg").remove();
        drawGraph(136);

        loaded = true;
        done = false;
    }
}

function anim(e) {
    if (!done) {
        if (loaded) {
            window.requestAnimationFrame(anim);

            // Limit speed of drawing
            if (frameCounter % 2 == 0) {
                drawLine(counter++);
            }

            // Reached the end of graph
            if (counter > 136) {
                done = true;
                loaded = false;
                counter = 1;
                frameCounter = 0;
            }

            frameCounter++;
        }
    }
}