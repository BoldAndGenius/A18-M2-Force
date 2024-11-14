
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





// Print a Menu Card using Switch Case Statement to select any one dish out of 4 items 

function print_menu(dish){
    console.log("Menu Card");
    console.log("Select One Dish Out of 4 Items - 1 - paneer, 2 - dal, 3 - juice, 4 - sweet ");
    // var dish = 'paneer'
    switch (dish){
        case 1:
            console.log("Eat Dal");
            break;
        case 2:
            console.log("Eat Paneer Masala");
            break;
        case 3:
            console.log("Drink Juice");
            break;
        case 4:
            console.log("Eat Sweet");
            break;
        default:
            console.log("Water");
        }
}
print_menu(2)











// Writ a program to find the average of even numbers from 1 to 100 


function average_even(start,end){
    // var end = 100 
    var sum = 0
    var total = 0
    for (var i= start; i<=end; i++ ){
        if (i % 2 == 0)
        {
            // console.log(start);
            sum = sum + i
            total = total + 1
        }
}
console.log("The Average is : ", sum/total );
}

average_even(1,100)





// Find the smallest number from 100 to 500 
var start = 100
var end = 500 
var smallest = 100000
for (var i = start; i<=end; i++){
    if (i < smallest){
        smallest = i
    }
}
console.log(smallest); 



// Using Function 

function smallest(start, end){
    // var start = 100
    // var end = 500 
    var smallest = 100000
    for (var i = start; i<=end; i++){
        if (i < smallest){
            smallest = i
        }
    }
    console.log(smallest); 
}
smallest(100,500)