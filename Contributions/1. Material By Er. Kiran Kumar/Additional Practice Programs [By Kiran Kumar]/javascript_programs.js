
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





// Write a Javascript Program to validate username & password and print login successful, if the condition is true, or else login failed.

function credential_validation(username1,password1){
    // var username = "Kiran"
    // var password = 1234 
    if (username1 == 'Kiran' && password1 == 1234)
    {
        console.log("Login Succesfful");
    } 
    else 
    {
        console.log("Login Failed"); 
    }
}
credential_validation("Kiran",12345)





// Voting Program Using JavaScript

var age = 18
if (age>18){
    console.log("Ready to Vote");
}
else{
    console.log("Not Eligible to Vote");
    
}
