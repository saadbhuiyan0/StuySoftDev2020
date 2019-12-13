// Saad Bhuiyan and Jionghao Wu
// SoftDev1 pd2
// K29 -- HTML+JS Integration
// 2019-12-

// Lo, what is this? Could it be a VALUE-ADDED-KEY2SUCCESS?!?!

var changeHeading = function(e) {
    var h = document.getElementById("h");
    h.innerHTML = this.innerHTML;
};

var removeItem = function(e) {
    this.remove();      
};

var lis = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++) {
    lis[i].addEventListener("mouseover", changeHeading);
    lis[i].addEventListener("mouseout", () => {
        document.getElementById("h").innerHTML = "Hello World!";
    });
    lis[i].addEventListener("click", removeItem);
};

var addItem = function(e) {
    var list = document.getElementById("thelist");
    var item = document.createElement("li");
    item.innerHTML = "WORD";
    item.addEventListener("mouseover", changeHeading);
    item.addEventListener("mouseout", () => {
        document.getElementById("h").innerHTML = "Hello World!";
    });
    item.addEventListener("click", removeItem);
    list.appendChild(item);
};

var button = document.getElementById("b");
button.addEventListener("click", addItem);

var fib = function(n) {
    if (n < 2) {
        return 1;
    }
    else {
        return fib(n-1) + fib(n-2);
    }
};

var addFib = function(e) {
    var fibList = document.getElementById("fiblist");
    var fibNumber = fibList.childNodes.length;
    var nextFib = document.createElement("li");
    // nextFib.innerHTML = fib(fibNumber);
    if (fibNumber < 3) {
        nextFib.innerHTML = fib(fibNumber);
    }
    else {
        var lastFib = fibList.lastChild.innerHTML;
        var beforeLastFib = fibList.lastChild.previousSibling.innerHTML;
        nextFib.innerHTML = parseInt(lastFib) + parseInt(beforeLastFib);
    }
    fibList.appendChild(nextFib);
    console.log(nextFib);
};

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);