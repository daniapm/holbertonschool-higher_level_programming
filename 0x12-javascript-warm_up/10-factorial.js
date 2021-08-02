#!/usr/bin/node
//  script that prints the addition of 2 integers
function factorial (n) {
  if (process.argv.length === 2 || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}
console.log(factorial(process.argv[2]));
