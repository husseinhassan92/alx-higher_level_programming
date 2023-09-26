#!/usr/bin/node

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
