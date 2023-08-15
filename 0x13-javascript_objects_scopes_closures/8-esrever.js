#!/usr/bin/node

exports.esrever = function (list) {
  let beg = 0;
  let end = list.length - 1;
  while (beg < end) {
    let temp = list[beg];
    list[beg] = list[end];
    list[end] = temp;
    beg++;
    end--;
  }
  return list;
};
