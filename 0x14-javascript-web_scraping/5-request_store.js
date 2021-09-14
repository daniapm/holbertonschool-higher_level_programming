#!/usr/bin/node
// script that display the status code of a GET request.
const request = require('request');
const fs = require('fs');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3])).on('error', function (response, body) {

});
