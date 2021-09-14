#!/usr/bin/node
// script that writes a string to a file.
const fs = require('fs');
const data = process.argv[3];
fs.writeFile(process.argv[2], data, (err) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
