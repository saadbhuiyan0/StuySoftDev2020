// Saad Bhuiyan and Jionghao Wu
// SoftDev1 pd2
// K29 -- HTML+JS Integration
// 2019-12-

// Lo, what is this? Could it be a VALUE-ADDED-KEY2SUCCESS?!?!

var changeHeading = function(e) {
    var h = document.getElementById("h");
    h.innerHTML = e;
};

var removeItem = function(e) {

};

var lis = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++) {
    lis[i].addEventListener("mouseover", changeHeading );
    lis[i].addEventListener("mouseout", () => {
        document.getElementById("h").innerHTML = "Hello World!";
    });
    lis[i].addEventListener("click", removeItem);
};

// var addItem = function(e) {
//     var list = document.getElementById("thelist");
//     var item = document.createElement("li");
//     ??? = "WORD";
//     ???
//     ...
//     ???
//     list.???(item);
// };

// var button = document.getElementById("b");
// button.addEventListener("click", addItem);

var fib = function(n) {
    if (n < 2) {
        return 1;
    }
    else {
        return fib(n-1) + fib(n-2);
    }
};

// var addFib = function(e) {
//     console.log(e);
//     ???
//     ... see QAF re: DYNAMIC PROGRAMMING...
//     ???
// };

// var fb = document.getElementById("fb");
// fb.addEventListener("click", addFib);