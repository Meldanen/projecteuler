//The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
//Find the sum of all the primes below two million.

const isPrime = num => {
    for(let i = 2, s = Math.sqrt(num); i <= s; i++)
        if(num % i === 0) return false; 
    return num > 1;
}

var primes = [];
var MAX = 2000000;
var sum = 0;

let i = 2;
while (i < MAX) {
    if (isPrime(i)) {
        sum += i
    }
    i++;
}
console.log(sum)
// Answer : 142913828922