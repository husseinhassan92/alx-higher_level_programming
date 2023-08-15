#!/usr/bin/node

const BaseSquare = require('./5-square');

module.exports = class Square extends BaseSquare {
  charPrint(c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
