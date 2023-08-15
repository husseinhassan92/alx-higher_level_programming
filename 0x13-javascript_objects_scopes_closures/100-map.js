#!/usr/bin/node
const list = require('./100-data').list;

const newList = list.map((x, ind) => x * ind);

console.log(list);
console.log(newList);
