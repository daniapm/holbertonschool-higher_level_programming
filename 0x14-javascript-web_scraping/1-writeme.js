#!/usr/bin/node
// script that writes a string to a file.
const fs = require('fs');
fs.writeFile(process.argv[2], 'utf-8', process.argv[3], (err) => {
  if (err) {
    console.log(err);
  }
});
