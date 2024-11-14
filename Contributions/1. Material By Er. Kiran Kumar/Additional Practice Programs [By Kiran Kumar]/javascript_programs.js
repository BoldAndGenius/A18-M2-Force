
// Sum of two numbers 

function sum_of_two_number(num1,num2){
    return num1 + num2
}
console.log(sum_of_two_number(10,30));



// Write a JavaScript Program to find the factorial of 10 

function factorial(num){
    // var num = 10
    var fact = 1
    for(var i = 1; i<=num; i++){
        fact = fact * i
    }
    console.log(fact);
}
factorial(10)