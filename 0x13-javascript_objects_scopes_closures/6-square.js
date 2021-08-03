#!/usr/bin/node

const SquareHeredado = require('./5-square');

//  class Square that defines a Square
class Square extends SquareHeredado {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
