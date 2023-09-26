#!/usr/bin/node

const filename = process.argv[2];
const fs = require('fs');
fs.writeFile(filename, process.argv[3], 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
