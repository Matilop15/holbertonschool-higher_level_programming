#!/usr/bin/node

// script that computes and prints a factorial
// The first argument is integer (argument can be cast as integer) used for computing the factorial

function factorial (num) {
  if (num === 0 || Number.isNaN(num)) return 1;
  return num * factorial(num - 1);
}
const num = parseInt(process.argv[2]);
console.log(factorial(num));
