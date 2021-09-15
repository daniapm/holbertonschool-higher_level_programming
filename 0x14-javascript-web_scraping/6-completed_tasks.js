#!/usr/bin/node
// script that display the status code of a GET request.
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const dict_task = {};
    const users = (JSON.parse(body));
    for (let i = 0; i < users.length; ++i) {
      const user_Id = users[i].userId;
      const completed = users[i].completed;
      if (completed) {
        dict_task[user_Id] = 0;
      }
      if (completed) {
        dict_task[user_Id]++;
      }
    }
    console.log(dict_task);
  }
});
