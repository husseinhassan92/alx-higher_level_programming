#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let i in list) {
    if (list[i] === searchElement) {
      counter++;
    }
  }
  return counter;
};
