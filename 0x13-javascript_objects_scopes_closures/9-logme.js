#!/usr/bin/node

let counter = -1;
exports.logMe = function (item) {
  counter++;
  console.log(counter + ': ' + item);
};
