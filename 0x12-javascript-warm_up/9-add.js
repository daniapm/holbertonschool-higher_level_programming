#!/usr/bin/node
//  script that prints a square
function add (a, b) {
  return (parseInt(a) + parseInt(b));
}
console.log(add(process.argv[2], process.argv[3]));
