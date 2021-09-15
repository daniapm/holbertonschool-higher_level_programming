#!/usr/bin/node
// script that prints all characters of a Star Wars movie
const request = require('request');
request(('https://swapi-api.hbtn.io/api/films/' + process.argv[2]), function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const results = (JSON.parse(body).characters);
    for (let i = 0; i < results.length; ++i) {
      request(results[i], function (error, response, body) {
        if (error) {
          console.log(error);
        } else if (response.statusCode === 200) {
          const results = (JSON.parse(body).name);
          console.log(results);
        }
      });
    }
  }
});
