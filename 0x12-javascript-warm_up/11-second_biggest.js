#!/usr/bin/node
//  script that prints the addition of 2 integers
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log('0');
} else {
  const num = process.argv.sort();
  const second = num.reverse();
  console.log(second[1]);
}
