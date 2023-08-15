#!/usr/bin/node

const dict = require('./101-data').dict;

let Dict = {};
for (let key in dict) {
  if (Dict[dict[key]] === undefined) {
    Dict[dict[key]] = [];
  }
  Dict[dict[key]].push(key);
}

console.log(Dict);
