#!/usr/bin/node
// prints a message depending of the number of arguments passed
if (process.argv[2] === undefined) {
  console.log(process.argv[2] + ' is ' + 'undefined');
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
