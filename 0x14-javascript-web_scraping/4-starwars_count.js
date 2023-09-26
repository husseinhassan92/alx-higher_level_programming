#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film in films) {
      const chars = films[film].characters;
      for (const char in chars) {
        if (chars[char].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
