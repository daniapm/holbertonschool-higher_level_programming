#!/usr/bin/node
//  script script that searches the second biggest integer in the list of arguments.
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  const num = process.argv.sort();
  const second = num.reverse();
  console.log(parseInt(second[1]));
}
