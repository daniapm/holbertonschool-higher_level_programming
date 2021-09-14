#!/usr/bin/node
// script that display the status code of a GET request.
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    let count = 0;
    const results = (JSON.parse(body).results);
    for (const result in results) {
      const data = results[result].characters;
      for (const id in data) {
        if (data[id] === 'https://swapi-api.hbtn.io/api/people/18/') {
          count++;
        }
      }
    }
    console.log(count);
  }
});
