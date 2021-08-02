#!/usr/bin/node
// prints a message depending of the number of arguments passed
if (process.argv[2] === undefined) {
  console.log('Not a number');
} else if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number:' + ' ' + parseInt(process.argv[2]));
}
