#!/usr/bin/node
// script that display the status code of a GET request.
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const dicttask = {};
    const users = (JSON.parse(body));
    for (let i = 0; i < users.length; ++i) {
      const userId = users[i].userId;
      const completed = users[i].completed;
      if (completed) {
        dicttask[userId] = 1;
      }
      if (completed) {
        dicttask[userId]++;
      }
    }
    console.log(dicttask);
  }
});
