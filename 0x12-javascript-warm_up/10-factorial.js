#!/usr/bin/node
// script that computes and prints a factorial
function myFactorial (n) {
  if (isNaN(n) || n < 2) {
    return 1;
  } else {
    return n * myFactorial(n - 1);
  }
}

console.log(myFactorial(process.argv[2]));
