// Saad Bhuiyan
// SoftDev1 p2
// K28 -- HTML+JS Integration
// 2019-12-11


// factorial(n) returns the factorial of the input number
var factorial = function(n) {
    if (n > 1) {
        return n * factorial(n - 1);
    }
    else {
        return 1;
    }
}


// fibonacci(n) returns the nth number in the fibonacci sequence
var fibonacci = function(n) {
    if (n == 0) {
        return 0;
    }
    else if (n == 1) {
        return 1;
    }
    else {
        return fibonacci(n - 1) + fibonacci(n - 2)
    }
}


// gcd(a,b) returns the greatest common divisor of the input numbers a and b
var gcd = function(a,b) {
    if (b > a) {var temp=a; a=b; b=temp;}
    var x = 1;
    var ans = 0;
    while (x <= a) {
        if ((a % x == 0) && (b % x == 0)) {
            ans = x;
        }
        x = x + 1;
    }
    return ans;
}


// array of students in SoftDev period 2
var studentsInPeriod2 = ["abedinM", "avrahamiB", "bhuiyanS", "caoW", "chanM", "chenE", "chenJ", "friedH", 
                         "huangP", "huangT", "linD", "linW", "lupeaD", "mosesB", "niA", "olinJ", "olteanuA", 
                         "rahmanM", "sontagC", "thompsonA", "wangD", "wuJ", "yusufovJ", "zenH"];

// randomStudent() returns a random student from the array studentsInPeriod2
var randomStudent = function() {
    randomNumber = Math.floor(Math.random() * studentsInPeriod2.length)
    return studentsInPeriod2[randomNumber]
}


// factorial button
var factorialButton = document.getElementById("factorialButton");
var factorialOutput = function() {
    console.log(factorial(5));
    document.getElementById("factorialOutput").innerHTML = factorial(5);
};
factorialButton.addEventListener("click", factorialOutput)


// fibonacci button
var fibonacciButton = document.getElementById("fibonacciButton");
var fibonacciOutput = function() {
    console.log(fibonacci(7));
    document.getElementById("fibonacciOutput").innerHTML = fibonacci(7);
};
fibonacciButton.addEventListener("click", fibonacciOutput)


// gcd button
var gcdButton = document.getElementById("gcdButton");
var gcdOutput = function() {
    console.log(gcd(111,18));
    document.getElementById("gcdOutput").innerHTML = gcd(111,18);
};
gcdButton.addEventListener("click", gcdOutput)


// randomStudent button
var randomStudentButton = document.getElementById("randomStudentButton");
var randomStudentOutput = function() {
    console.log(randomStudent());
    document.getElementById("randomStudentOutput").innerHTML = randomStudent();
};
randomStudentButton.addEventListener("click", randomStudentOutput)