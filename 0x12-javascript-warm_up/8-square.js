#!/usr/bin/node
// script that prints 3 lines The first line: “C is fun”
if (isNaN(process.argv[2])) {
	console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
	console.log('X'.repeat(parseInt(process.argv[2])));
}
}
