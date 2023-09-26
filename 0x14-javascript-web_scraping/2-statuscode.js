#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
request.get(url).on('response', function (response) {
  console.log('code:', response.statusCode);
});
