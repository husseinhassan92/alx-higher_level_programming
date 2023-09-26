#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const dict = {};
    for (const todo in todos) {
      if (todos[todo].completed) {
        if (dict[todos[todo].userId] === undefined) {
          dict[todos[todo].userId] = 1;
        } else {
          dict[todos[todo].userId] += 1;
        }
      }
    }
    console.log(dict);
  }
});
