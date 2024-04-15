#!/usr/bin/node
const SquareParent = require('./5-square');

class Square extends SquareParent {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let a = 0; a < this.height; a++) {
      let row = '';
      for (let b = 0; b < this.width; b++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
