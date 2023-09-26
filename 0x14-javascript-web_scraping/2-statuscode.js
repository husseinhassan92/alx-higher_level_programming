#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (response) {
  console.log('statusCode:', response.statusCode);
});
