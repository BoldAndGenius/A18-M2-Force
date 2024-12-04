function factorial(num){
    // var num = 10
    var fact = 1
    for(var i = 1; i<=num; i++){
        fact = fact * i
    }
    console.log(fact);
}
factorial(10)